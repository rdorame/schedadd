from rest_framework.permissions import BasePermission
from .models import Son

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Son):
            return obj.parentID == request.user
        return obj.parentID == request.user
