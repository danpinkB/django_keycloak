from django.http.response import HttpResponse
from .keycloak_decorator import has_keycloak_role, has_keycloak_access_to_resource


@has_keycloak_role('admin')
def custom_admin_role_page(request):
    return HttpResponse('custom_admin_page')


@has_keycloak_access_to_resource('account_resource', 'profile')
def custom_admin_permission_page(request):
    return HttpResponse('custom_admin_page')
