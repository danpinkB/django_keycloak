from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from keycloak import KeycloakOpenID, KeycloakAuthenticationError

from .keycloak_helper import KeycloakHelper
from django.conf import settings

KEYCLOAK_REFRESH_TOKEN_NAME = settings.KEYCLOAK_REFRESH_TOKEN_NAME
KEYCLOAK_ACCESS_TOKEN_NAME = settings.KEYCLOAK_ACCESS_TOKEN_NAME


class KeycloakAuthBackend(ModelBackend):
    def __init__(self):
        self._keycloak_helper = KeycloakHelper()

    def authenticate(self, request: WSGIRequest, username=None, password=None, **kwargs):
        try:
            if not self._keycloak_helper.has_role("admin", request.COOKIES.get(KEYCLOAK_ACCESS_TOKEN_NAME)):
                return
            if username is None:
                username = kwargs.get(User.USERNAME_FIELD)
            if username is None or password is None:
                return
            user = User.objects.get(username=username)
            return user
        except KeycloakAuthenticationError:
            return
        except User.DoesNotExist:
            user = User(username=username)
            user.is_staff = True
            user.save()
            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
