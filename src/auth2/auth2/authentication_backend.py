from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User, Permission
from django.core.handlers.wsgi import WSGIRequest
from keycloak import KeycloakOpenID, KeycloakAuthenticationError

from .keycloak_helper import KeycloakHelper
from django.conf import settings


class KeycloakAuthBackend(ModelBackend):
    def __init__(self):
        self._keycloak_helper = KeycloakHelper()

    def authenticate(self, request: WSGIRequest, username=None, password=None, **kwargs):
        token: str
        try:
            token = self._keycloak_helper.token(username, password)['access_token']
            user = User.objects.get(username=username)
            print("FINDED")
            print(user)
            return user
        except KeycloakAuthenticationError:
            print("ERRRR")
            return
        except User.DoesNotExist:
            roles = self._keycloak_helper.get_roles(token)
            user = User(username=username)
            user.save()
            if 'superuser' in roles:
                user.is_superuser = True
            elif 'admin' in roles:
                for perm in Permission.objects.all():
                    user.user_permissions.add(perm)
            else:
                user.is_staff = True
            user.save()
            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
