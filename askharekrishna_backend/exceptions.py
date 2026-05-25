from rest_framework.exceptions import Throttled
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None and isinstance(exc, Throttled):
        response.data = {
            'message': 'Too many requests',
            'detail': 'Rate limit exceeded. Please wait before trying again.',
            'available_in_seconds': getattr(exc, 'wait', None),
        }

    return response