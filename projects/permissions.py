from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

    # if the request method is safe (like GET because it doesn't change the database),
    # otherwise, make sure that the request user is the owner of the thing being requested
    # go to views to update permission stuff