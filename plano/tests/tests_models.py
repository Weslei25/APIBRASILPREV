from django.test import TestCase
from plano.models import PlanoModel
from produto.models import ProdutoModel
from cliente.models import ClienteModel
from django.urls import reverse
import json
from datetime import date, timedelta


class ClienteTesteCase(TestCase):
    
    def setUp(self) -> None:

        self.cliente = ClienteModel.objects.create(
            cpf="12345678912",
            nome="Weslei",
            sexo="M",
            email="wesleisantos25@gmail.com",
            dataDeNascimento="1996-10-26",
            rendaMensal=5.000
        )

                
        self.produto = ProdutoModel.objects.create(
            nome= "Brasilprev Longo Prazo",
            susep="15414.900840/2018-17",
            expiracaoDeVenda = "2023-01-16",
            valorMinimoAporteInicial= 2899.5,
            valorMinimoAporteExtra = 2899.5, 
            idadeDeEntrada =18, 
            idadeDeSaida =  60,
            carenciaInicialDeResgate = 60, 
            carenciaEntreResgates = 30 
        )

        self.plano = PlanoModel(
            aporte= 50.000,
            dataDaContratacao= "2022-04-05",
            produto=ProdutoModel.objects.get(id=self.produto.id),
            cliente=ClienteModel.objects.get(id=self.cliente.id)
        )
        self.plano.save()
    
    def test_retorno_name(self):
        cliente = ClienteModel.objects.get(id=self.cliente.id)
        self.assertEquals(cliente.__str__(), 'Weslei')

    def test_cpf_cliente(self):
        cliente = ClienteModel.objects.filter(id=self.cliente.id).values()[0]
        self.assertEquals(len(cliente['cpf']), 11)
    
    def test_email_cliente(self):
        cliente = ClienteModel.objects.filter(id=self.cliente.id).values()[0]
        self.assertEquals(len(cliente['sexo']), 1)
    
    def test_renda_float(self):
        cliente = ClienteModel.objects.filter(id=self.cliente.id).values()[0]
        self.assertNotEqual(type(cliente['rendaMensal']), float)
