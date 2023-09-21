from rest_framework.permissions import BasePermission

class BookAddListPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.has_perm('books.add_book')
               and request.user.has_perm('books.view_book'))


class BookUpdatePermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.has_perm('books.change_book')
               and request.user.has_perm('books.view_book'))


class SectionAddListPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.has_perm('books.add_section')
               and request.user.has_perm('books.view_section'))


class SectionUpdatePermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.has_perm('books.change_section')
               and request.user.has_perm('books.view_section'))
