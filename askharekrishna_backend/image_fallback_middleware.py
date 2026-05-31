import json
from typing import Any

from django.conf import settings


class ApiImageFallbackMiddleware:
    """Ensure API JSON payloads always return an image URL for empty image fields."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return self.process_response(request, response)

    @staticmethod
    def _is_image_key(key: str) -> bool:
        lowered = key.lower()
        return (
            'image' in lowered
            or 'thumbnail' in lowered
            or 'cover' in lowered
            or lowered.endswith('banner')
        )

    @staticmethod
    def _is_missing(value: Any) -> bool:
        return value is None or (isinstance(value, str) and value.strip() == '')

    def _apply_fallback(self, node: Any, fallback_url: str) -> Any:
        if isinstance(node, dict):
            for key, value in node.items():
                if self._is_image_key(key) and self._is_missing(value):
                    node[key] = fallback_url
                else:
                    node[key] = self._apply_fallback(value, fallback_url)
            return node

        if isinstance(node, list):
            return [self._apply_fallback(item, fallback_url) for item in node]

        return node

    def process_response(self, request, response):
        content_type = response.get('Content-Type', '')
        if 'application/json' not in content_type:
            return response

        fallback_path = getattr(
            settings,
            'DEFAULT_FALLBACK_IMAGE_PATH',
            '/media/debate/article/harekrishnaPreaching.jpg',
        )
        fallback_base = getattr(settings, 'PUBLIC_MEDIA_BASE_URL', '').rstrip('/')

        if fallback_path.startswith('http://') or fallback_path.startswith('https://'):
            fallback_url = fallback_path
        elif fallback_base:
            fallback_url = f"{fallback_base}{fallback_path}"
        else:
            fallback_url = request.build_absolute_uri(fallback_path)

        try:
            payload = json.loads(response.content.decode('utf-8'))
        except (ValueError, AttributeError, UnicodeDecodeError):
            return response

        transformed = self._apply_fallback(payload, fallback_url)
        response.content = json.dumps(transformed).encode('utf-8')
        response['Content-Length'] = str(len(response.content))
        return response
