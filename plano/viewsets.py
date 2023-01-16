from rest_framework import permissions
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

from plano.serializeres import PlanoSerializer, AporteExtraSerializer, ResgateSerializer
from plano.models import PlanoModel, ClienteModel, ProdutoModel, AporteExtraModel, ResgateModel

import json
from datetime import date, timedelta
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseNotFound

class PlanoViewSet(viewsets.ModelViewSet):
    #As regras da contratação como valor de aporte, idade mínima de entrada e saída etc., devem ser levadas em consideração.
    
    def create(self, request, *args, **kwargs):

        json_data = json.loads(request.body)

        #Não será possível contratar um produto com prazo de venda expirado.
        verificate_data = ProdutoModel.objects.filter(id=json_data["produto"]).values()[0]

        expiracaoDeVenda = verificate_data['expiracaoDeVenda']
        if expiracaoDeVenda < date.today():
            return JsonResponse(data={"erro":"Prazo de venda expirado",
                                      "data":expiracaoDeVenda}, status=status.HTTP_404_NOT_FOUND)

        valorMinimoAporteInicial = verificate_data['valorMinimoAporteInicial']
        if json_data['aporte'] < valorMinimoAporteInicial:
            return JsonResponse(data={"erro":"Valor minimo não atingido",
                                      "valor":valorMinimoAporteInicial}, status=status.HTTP_402_PAYMENT_REQUIRED)

        verificate_cliente = ClienteModel.objects.filter(id=json_data["cliente"]).values()[0]

        dataDeNascimento = verificate_cliente['dataDeNascimento']

        if calculateAge(dataDeNascimento) < verificate_data['idadeDeEntrada'] or calculateAge(dataDeNascimento) > verificate_data['idadeDeSaida']:
            return JsonResponse(data={"erro":"Idade não permitida",
                                      "idade":calculateAge(dataDeNascimento),
                                      "idadeDeEntrada":f"{verificate_data['idadeDeEntrada']}",
                                      "idadeDeSaida":f"{verificate_data['idadeDeSaida']}"}, status=status.HTTP_402_PAYMENT_REQUIRED)
        
        plano = PlanoModel(
                        produto=ProdutoModel.objects.get(id=json_data['produto']),
                        cliente=ClienteModel.objects.get(id=json_data['cliente']),
                        aporte=json_data['aporte']
                        )

        plano.save(force_insert=True)
        return JsonResponse(data={"id":"{}".format((plano.pk))}, status=status.HTTP_201_CREATED)

        
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

class AporteExtraViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):

        json_data = json.loads(request.body)

        #Deve ser validado o valor mínimo de aporte extra do produto.
        verificate_aport = PlanoModel.objects.filter(id=json_data["plano"]).values()[0]
        verificate_aport_prod = ProdutoModel.objects.filter(id=verificate_aport['produto_id']).values()[0]
        valorMinimoAporteExtra = verificate_aport_prod['valorMinimoAporteExtra']

        if json_data['valorAporte'] < valorMinimoAporteExtra:
            return JsonResponse(data={"erro":"Valor minimo não atingido",
                                      "valor":valorMinimoAporteExtra}, status=status.HTTP_402_PAYMENT_REQUIRED)

        aporte_extra = AporteExtraModel(
                        plano=PlanoModel.objects.get(id=json_data['plano']),
                        cliente=ClienteModel.objects.get(id=json_data['cliente']),
                        valorAporte=json_data['valorAporte']
                        )
        
        aporte_extra.save(force_insert=True)

        #Atualiza a tabela de planos
        valor_aport = float(json_data['valorAporte'])
        valor_aport2 = float(verificate_aport['aporte'])
        aport_update = valor_aport + valor_aport2

        PlanoModel.objects.filter(id=verificate_aport['id']).update(aporte=aport_update)

        return JsonResponse(data={"id":"{}".format((aporte_extra.pk))}, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        return Response(data={"Error":f"Method '#{request.method}#' not allowed."}, status=status.HTTP_401_UNAUTHORIZED)
    
    def destroy(self, request, *args, **kwargs):
        return Response(data={"Error":f"Method '#{request.method}#' not allowed."}, status=status.HTTP_401_UNAUTHORIZED)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
        
    queryset = AporteExtraModel.objects.all()
    serializer_class = AporteExtraSerializer
    permission_classes = [permissions.IsAuthenticated]

class ResgateViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):

        json_data = json.loads(request.body)

        try:
            verificate_plano = PlanoModel.objects.filter(id=json_data["plano"]).values()[0]
            verificate_prod = ProdutoModel.objects.filter(id=verificate_plano['produto_id']).values()[0]
        except IndexError:
            return JsonResponse(data={"erro":"Nenhuma informação encontrada"},status=status.HTTP_401_UNAUTHORIZED)

        carencia = date.today()
        td = timedelta(verificate_prod['carenciaInicialDeResgate'])
        data_possivel = carencia + td
        
        #Devem ser validados os prazos de carência para resgate
        if data_possivel < date.today():
            return JsonResponse(data={"erro":"Carencia em vigor",
                                      "carencia":carencia}, status=status.HTTP_401_UNAUTHORIZED)

        if json_data['valorResgate'] > verificate_plano['aporte']:
            return JsonResponse(data={"erro":"Valor solicitado excede o limite",
                                      "valorTotal":verificate_plano['aporte']}, status=status.HTTP_401_UNAUTHORIZED)
        resgate = ResgateModel(
                        plano=PlanoModel.objects.get(id=json_data['plano']),
                        valorResgate=json_data['valorResgate']
                        )
        
        resgate.save(force_insert=True)

        #Atualiza tabela de planos
        aporte = float(verificate_plano['aporte'])
        valorResgate = float(json_data['valorResgate'])
        aport_update = aporte - valorResgate

        PlanoModel.objects.filter(id=json_data['plano']).update(aporte=aport_update)

        return JsonResponse(data={"id":"{}".format((resgate.pk))}, status=status.HTTP_201_CREATED)

    queryset = ResgateModel.objects.all()
    serializer_class = ResgateSerializer
    permission_classes = [permissions.IsAuthenticated]

def calculateAge(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
    return age 
        