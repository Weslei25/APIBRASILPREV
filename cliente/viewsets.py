from rest_framework import permissions
from rest_framework import viewsets, status
from rest_framework.response import Response

from cliente.serializeres import ClienteSerializer
from cliente.models import ClienteModel

from django.http import HttpResponse, Http404, JsonResponse

class ClienteViewSet(viewsets.ModelViewSet):

    #So permite permissions.SAFE_METHODS
    def create(self, request, *args, **kwargs):
        if request.method in permissions.SAFE_METHODS:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(data={"Erro":"Metodo não permitido"}, status=status.HTTP_401_UNAUTHORIZED)

    queryset = ClienteModel.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]
