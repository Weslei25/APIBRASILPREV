from django.test import TestCase
from produto.models import ProdutoModel
from cliente.models import ClienteModel

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
            idadeDeEntrada = 18, 
            idadeDeSaida =  60,
            carenciaInicialDeResgate = 60, 
            carenciaEntreResgates = 30 
        )
    

    def test_assert_produto(self):
        produto = ProdutoModel.objects.filter(id=self.produto.id).values()[0]
        self.assertEquals(len(produto['susep']), 20)
        self.assertEquals(produto['nome'].__str__(), self.produto.nome)
        self.assertTrue(produto['id'] == self.produto.id)
        self.assertTrue(produto['valorMinimoAporteInicial'] > 1000)
        self.assertTrue(produto['idadeDeEntrada'] >= 18)
