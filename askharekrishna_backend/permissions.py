from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """Allow public reads; require staff + model permissions for writes."""

    method_permission_map = {
        'POST': 'add',
        'PUT': 'change',
        'PATCH': 'change',
        'DELETE': 'delete',
    }

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        user = request.user
        if not (user and user.is_authenticated and user.is_staff):
            return False

        perm_action = self.method_permission_map.get(request.method)
        if not perm_action:
            return True

        queryset = getattr(view, 'queryset', None)
        if queryset is None and hasattr(view, 'get_queryset'):
            try:
                queryset = view.get_queryset()
            except Exception:
                queryset = None

        model = getattr(queryset, 'model', None)
        if model is None:
            # If model metadata is unavailable, fall back to staff-only check.
            return True

        perm_codename = f"{model._meta.app_label}.{perm_action}_{model._meta.model_name}"
        return user.has_perm(perm_codename)