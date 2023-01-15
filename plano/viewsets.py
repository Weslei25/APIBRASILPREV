from rest_framework import permissions
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

from plano.serializeres import PlanoSerializer
from plano.models import PlanoModel

import json

from django.http import HttpResponse, Http404, JsonResponse

class ProdutoViewSet(viewsets.ModelViewSet):

    #Não será possível contratar um produto com prazo de venda expirado.
    #As regras da contratação como valor de aporte, idade mínima de entrada e saída etc., devem ser levadas em consideração.
    
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
    
    queryset = PlanoModel.objects.all()
    serializer_class = PlanoSerializer
    permission_classes = [permissions.IsAuthenticated]