from django.test import TestCase
from cliente.models import ClienteModel
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from rest_framework import status
from django.shortcuts import redirect, render
from rest_framework.test import APIClient
from rest_framework.test import RequestsClient

class ClienteTesteCase(TestCase):
    
    def setUp(self) -> None:
        ClienteModel.objects.create(cpf="12345678912",
                                    nome="Weslei",
                                    sexo="M",
                                    email="wesleisantos25@gmail.com",
                                    dataDeNascimento="2023-01-14",
                                    rendaMensal="5.000"
        )

    def test_retorno_uuid(self):
        cliente = ClienteModel.objects.get(nome="Weslei")
        self.assertEquals(cliente.__str__(), 'Weslei')

    def test_cpf_cliente(self):
        cliente = ClienteModel.objects.filter(nome="Weslei").values()[0]
        self.assertEquals(len(cliente['cpf']), 11)
    
    def test_email_cliente(self):
        cliente = ClienteModel.objects.filter(nome="Weslei").values()[0]
        self.assertEquals(len(cliente['sexo']), 1)
    
    def test_renda_float(self):
        cliente = ClienteModel.objects.filter(nome="Weslei").values()[0]
        self.assertNotEqual(type(cliente['rendaMensal']), float)

    def test_pessoa_form_invalido(self):
        form = ClienteModel(cpf="12345678912")
        self.assertFalse(form.validate_unique())