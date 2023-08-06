from rest_framework import viewsets


class BankViewSet(viewsets.ModelViewSet):

    keycloak_roles = {
        'GET': ['admin']
    }

    def list(self, request):
        """
        Overwrite method
        You can especify your rules inside each method
        using the variable 'request.roles' that means a
        list of roles that came from authenticated token.
        See the following example bellow:
        """
        # list of token roles
        print(request.roles)

        # Optional: get userinfo (SUB attribute from JWT)
        print(request.userinfo)

        return super().list(self, request)