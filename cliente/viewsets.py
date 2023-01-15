from rest_framework import permissions
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

from cliente.serializeres import ClienteSerializer
from cliente.models import ClienteModel

from django.http import HttpResponse, Http404, JsonResponse
import json

class ClienteViewSet(viewsets.ModelViewSet):

    #Somente visualização
    def create(self, request, *args, **kwargs):
        return Response(data={"Error":f"Method '#{request.method}#' not allowed."}, status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, *args, **kwargs):
        return Response(data={"Error":f"Method '#{request.method}#' not allowed."}, status=status.HTTP_401_UNAUTHORIZED)
    
    def destroy(self, request, *args, **kwargs):
        return Response(data={"Error":f"Method '#{request.method}#' not allowed."}, status=status.HTTP_401_UNAUTHORIZED)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    queryset = ClienteModel.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]


class CadastrarClienteViewSet(viewsets.ModelViewSet):
    
    def create(self, request, *args, **kwargs):
        json_data = json.loads(request.body)
        serializado = ClienteModel.objects.create(**json_data)
        data = {"id":"{}".format(serializado.id)}
        return JsonResponse(data=data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        return Response(data={"Error":f"Method '#{request.method}#' not allowed."}, status=status.HTTP_401_UNAUTHORIZED)
    
    def destroy(self, request, *args, **kwargs):
        return Response(data={"Error":f"Method '#{request.method}#' not allowed."}, status=status.HTTP_401_UNAUTHORIZED)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    queryset = ClienteModel.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]