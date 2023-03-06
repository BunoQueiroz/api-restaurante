from rest_framework import viewsets
from clients.serializers import ClientSerializer
from clients.models import Client

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
