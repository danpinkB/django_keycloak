import functools
from typing import List

from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect
from django.contrib import messages
from .keycloak_helper import KeycloakHelper
_helper = KeycloakHelper()
KEYCLOAK_REFRESH_TOKEN_NAME = settings.KEYCLOAK_REFRESH_TOKEN_NAME
KEYCLOAK_ACCESS_TOKEN_NAME = settings.KEYCLOAK_ACCESS_TOKEN_NAME


def has_keycloak_role(role: str):
    def has_keycloak_role_(view_func):
        @functools.wraps(view_func)
        def wrapper(request: WSGIRequest, *args, **kwargs):
            if _helper.has_role(role, request.COOKIES.get(KEYCLOAK_ACCESS_TOKEN_NAME)):
                return view_func(request, *args, **kwargs)
            return redirect("accounts:profile")
        return wrapper
    return has_keycloak_role_


def has_keycloak_access_to_resource(resource_name: str, scope_name: str):
    def has_keycloak_role_(view_func):
        @functools.wraps(view_func)
        def wrapper(request: WSGIRequest, *args, **kwargs):
            if _helper.has_access_to_resource(resource_name, scope_name, request.COOKIES.get(KEYCLOAK_ACCESS_TOKEN_NAME)):
                return view_func(request, *args, **kwargs)
            return redirect("accounts:profile")
        return wrapper

    return has_keycloak_role_
