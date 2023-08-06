from warnings import filters

from django.contrib.auth.models import User, User
from rest_framework import viewsets, serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['name']


class InventoryViewSet(viewsets.ModelViewSet):
    keycloak_scopes = {
        'GET': 'account_resource#profile'
    }
    serializer_class = GroupSerializer
    queryset = User.objects.all().order_by('id')