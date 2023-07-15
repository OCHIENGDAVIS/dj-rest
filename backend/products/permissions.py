from rest_framework import permissions


class IsStaffEdidtorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        if user.is_staff:
            print(user.get_all_permissions)
            if user.has_perm('products.view_product'):
                return True
            if user.has_perm('products.change_product'):
                return True
            if user.has_perm('products.add_product'):
                return False
            if user.has_perm('products.delete_product'):
                return True
            return False
        print(user.get_all_permissions)
        return False

    # def has_object_permission(self, request, view, obj):
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #     return obj.owner == request.user
