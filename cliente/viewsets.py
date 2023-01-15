from rest_framework import permissions
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

from cliente.serializeres import ClienteSerializer
from cliente.models import ClienteModel

from django.http import HttpResponse, Http404, JsonResponse

class ClienteViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        if request.method not in permissions.SAFE_METHODS:
            return Response(data={"Error":f"Method '#{request.method}#' not allowed."}, status=status.HTTP_401_UNAUTHORIZED)

    queryset = ClienteModel.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]
