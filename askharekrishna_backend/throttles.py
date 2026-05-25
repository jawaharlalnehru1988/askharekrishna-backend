from rest_framework.throttling import SimpleRateThrottle, UserRateThrottle


class AuthenticatedUserRateThrottle(UserRateThrottle):
    scope = 'user'

    def get_cache_key(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return None

        return self.cache_format % {
            'scope': self.scope,
            'ident': request.user.pk,
        }


class ClientIPRateThrottle(SimpleRateThrottle):
    scope = 'ip'

    def get_cache_key(self, request, view):
        return self.cache_format % {
            'scope': self.scope,
            'ident': self.get_ident(request),
        }