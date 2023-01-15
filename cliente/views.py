from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import authentication, permissions
import json

from cliente.serializeres import ClienteSerializer
from cliente.models import ClienteModel

from django.http import HttpResponse, Http404, JsonResponse

class CadastrarClienteView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        json_data = json.loads(request.body)
        serializado = ClienteModel.objects.create(**json_data)
        data = {"id":"{}".format(serializado.id)}
        return JsonResponse(data=data, status=status.HTTP_201_CREATED)