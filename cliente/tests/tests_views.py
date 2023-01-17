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



class TokenViewTestCase(TestCase):

    def test_status_code_200_token_refresh_view(self):
        response = self.client.get(reverse('token_refresh_view'))
        self.assertEquals(response.status_code, 405)

    def test_status_code_200_token_view(self):
        response = self.client.get(reverse('token_view'))
        self.assertEquals(response.status_code, 405)

class ClientePostTestCase(TestCase):
    
    def test_force_acesso_cliente(self):

        response = self.client.get('/api/cliente/show_clientes/')
        self.assertEquals(response.status_code, 401)