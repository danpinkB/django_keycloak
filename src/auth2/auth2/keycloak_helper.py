from django.conf import settings
from keycloak import KeycloakOpenID
from keycloak.uma_permissions import AuthStatus


class KeycloakHelper:

    def __init__(self):
        self._config = settings.KEYCLOAK_CONFIG
        self._connection = KeycloakOpenID(server_url=self._config['KEYCLOAK_SERVER_URL'],
                                           client_id=self._config['KEYCLOAK_CLIENT_ID'],
                                           realm_name=self._config['KEYCLOAK_REALM'],
                                           client_secret_key=self._config['KEYCLOAK_CLIENT_SECRET_KEY'])
        self._connection.load_authorization_config(self._config['KEYCLOAK_AUTHORIZATION_CONFIG'])
        self._KEYCLOAK_PUBLIC_KEY = settings.KEYCLOAK_CLIENT_PUBLIC_KEY
        self._jwt_options = {"verify_signature": True, "verify_aud": True, "verify_exp": True}

    def token(self, username: str, password: str) -> dict:
        return self._connection.token(username, password)

    def get_userinfo(self, access_token: str) -> dict:
        return self._connection.userinfo(access_token)

    def has_access_to_resource(self, resource_name: str, scope_name: str, access_token: str)->bool:
        # print(self._connection.has_uma_access(access_token, "account_resource#profile"))
        status: AuthStatus = self._connection.has_uma_access(access_token, f'{resource_name}#{scope_name}')
        return status.is_authorized

    def get_roles(self, access_token: str):
        return self._connection.decode_token(access_token, key=self._KEYCLOAK_PUBLIC_KEY, options=self._jwt_options).get("realm_access").get("roles")

    def has_role(self, role: str, access_token: str) -> bool:
        token_info = self._connection.decode_token(access_token, key=self._KEYCLOAK_PUBLIC_KEY, options=self._jwt_options)
        return role in token_info.get("realm_access").get("roles")

    def logout(self, refresh_token: str) -> dict:
        return self._connection.logout(refresh_token)

