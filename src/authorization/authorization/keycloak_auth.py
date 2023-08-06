from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseRedirect
from .keycloak_helper import KeycloakHelper
from django.conf import settings

_keycloak_helper = KeycloakHelper()


KEYCLOAK_REFRESH_TOKEN_NAME = settings.KEYCLOAK_REFRESH_TOKEN_NAME
KEYCLOAK_ACCESS_TOKEN_NAME = settings.KEYCLOAK_ACCESS_TOKEN_NAME


def keycloak_login(request: WSGIRequest, **kwargs) -> HttpResponseRedirect:
    res: HttpResponseRedirect = admin.site.login(request, **kwargs)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        token = _keycloak_helper.token(username, password)
        res.set_cookie(KEYCLOAK_ACCESS_TOKEN_NAME, token['access_token'])
        res.set_cookie(KEYCLOAK_REFRESH_TOKEN_NAME, token['refresh_token'])
    return res


def keycloak_logout(request: WSGIRequest, **kwargs) -> HttpResponseRedirect:
    res: HttpResponseRedirect = admin.site.logout(request, **kwargs)
    if request.method == 'POST':
        if KEYCLOAK_REFRESH_TOKEN_NAME in res.cookies:
            _keycloak_helper.logout(res.cookies.get(KEYCLOAK_REFRESH_TOKEN_NAME))
            res.delete_cookie(KEYCLOAK_ACCESS_TOKEN_NAME)
            res.delete_cookie(KEYCLOAK_REFRESH_TOKEN_NAME)
    return res
