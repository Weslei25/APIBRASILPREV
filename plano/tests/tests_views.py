from django.test import TestCase
from plano.models import PlanoModel, AporteExtraModel, ResgateModel
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
            valorMinimoAporteInicial= 1000.5,
            valorMinimoAporteExtra = 500.0, 
            idadeDeEntrada =18, 
            idadeDeSaida =  60,
            carenciaInicialDeResgate = 60, 
            carenciaEntreResgates = 30 
        )

        self.plano = PlanoModel(
            aporte= 550.5,
            dataDaContratacao= "2022-01-16",
            produto=ProdutoModel.objects.get(id=self.produto.id),
            cliente=ClienteModel.objects.get(id=self.cliente.id)
        )
        
        self.plano.save()

        self.aporte_extra = AporteExtraModel(
            valorAporte= 500.000,
            plano=PlanoModel.objects.get(id=self.plano.id),
            cliente=ClienteModel.objects.get(id=self.cliente.id)
        )

        self.aporte_extra.save()

        self.resgate = ResgateModel(
            valorResgate= 500.000,
            plano=PlanoModel.objects.get(id=self.plano.id)
        )

        self.resgate.save()

    def test_assert_produto(self):
        produto = ProdutoModel.objects.filter(id=self.produto.id).values()[0]
        self.assertEquals(len(produto['susep']), 20)
        self.assertEquals(produto['nome'].__str__(), self.produto.nome)
        self.assertTrue(produto['id'] == self.produto.id)
        self.assertTrue(produto['valorMinimoAporteInicial'] > 1000)

    def test_assert_plano(self):
        plano = PlanoModel.objects.filter(id=self.plano.id).values()[0]
        produto = ProdutoModel.objects.filter(id=self.produto.id).values()[0]
        cliente = ClienteModel.objects.filter(id=self.cliente.id).values()[0]

        self.assertTrue(produto['expiracaoDeVenda'] >= plano['dataDaContratacao'])
        self.assertFalse(produto['expiracaoDeVenda'] <= plano['dataDaContratacao'])
        self.assertFalse(produto['valorMinimoAporteInicial'] < plano['aporte'])

        birthDate = cliente['dataDeNascimento']
        today = date.today() 
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
        self.assertFalse(age < produto['idadeDeEntrada'] or age > produto['idadeDeSaida'])

    def test_assert_aporte_extra(self):
        plano = PlanoModel.objects.filter(id=self.plano.id).values()[0]
        produto = ProdutoModel.objects.filter(id=self.produto.id).values()[0]
        cliente = ClienteModel.objects.filter(id=self.cliente.id).values()[0]
        aporte_extra = AporteExtraModel.objects.filter(id=self.aporte_extra.id).values()[0]

        self.assertTrue(aporte_extra['valorAporte'] >= produto['valorMinimoAporteExtra'])

    def test_assert_resgate(self):
        plano = PlanoModel.objects.filter(id=self.plano.id).values()[0]
        produto = ProdutoModel.objects.filter(id=self.produto.id).values()[0]
        cliente = ClienteModel.objects.filter(id=self.cliente.id).values()[0]
        aporte_extra = AporteExtraModel.objects.filter(id=self.aporte_extra.id).values()[0]

        carencia = date.today()
        td = timedelta(produto['carenciaInicialDeResgate'])
        print(td)
        data_possivel = carencia + td

        self.assertFalse(data_possivel < date.today())