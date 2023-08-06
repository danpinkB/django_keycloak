from django.conf import settings
from keycloak import KeycloakOpenID
from keycloak.uma_permissions import AuthStatus


class KeycloakHelper:

    def __init__(self):
        self._config = settings.KEYCLOAK_CONFIG
        self._connection = KeycloakOpenID(server_url=self._config['SERVER_URL'],
                                           client_id=self._config['CLIENT_ID'],
                                           realm_name=self._config['REALM_NAME'],
                                           client_secret_key=self._config['CLIENT_SECRET_KEY'])
        self._connection.load_authorization_config(self._config['AUTHORIZATION_CONFIG'])
        self._KEYCLOAK_PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\n" + self._config['PUBLIC_KEY'] + "\n-----END PUBLIC KEY-----"
        self._jwt_options = {"verify_signature": True, "verify_aud": False, "verify_exp": True}

    def token(self, username: str, password: str) -> dict:
        return self._connection.token(username, password)

    def get_userinfo(self, access_token: str) -> dict:
        return self._connection.userinfo(access_token)

    def has_access_to_resource(self, resource_name: str, scope_name: str, access_token: str)->bool:
        # print(self._connection.has_uma_access(access_token, "account_resource#profile"))
        status: AuthStatus = self._connection.has_uma_access(access_token, f'{resource_name}#{scope_name}')
        return status.is_authorized

    def has_role(self, role: str, access_token: str) -> bool:
        token_info = self._connection.decode_token(access_token, key=self._KEYCLOAK_PUBLIC_KEY, options=self._jwt_options)
        return role in token_info.get("realm_access").get("roles")

    def logout(self, refresh_token: str) -> dict:
        return self._connection.logout(refresh_token)

