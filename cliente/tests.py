from django.test import TestCase

# Create your tests here.

from cliente.models import ClienteModel

class ClienteModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        ClienteModel.objects.create(first_name='Big', last_name='Bob')

    def test_create_client(self):
        pass

    def test_first_name_label(self):
        cliente = ClienteModel.objects.get(id=1)
        field_label = cliente._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_date_of_death_label(self):
        cliente=ClienteModel.objects.get(id=1)
        field_label = cliente._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'died')

    def test_first_name_max_length(self):
        cliente = ClienteModel.objects.get(id=1)
        max_length = cliente._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        cliente = ClienteModel.objects.get(id=1)
        expected_object_name = f'{cliente.last_name}, {cliente.first_name}'
        self.assertEquals(expected_object_name, str(cliente))

    def test_get_absolute_url(self):
        cliente = ClienteModel.objects.get(id=1)
        self.assertEquals(cliente.get_absolute_url(), '/api/cliente/1')


from django.urls import reverse

class AuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crie 13 clientes para testes de paginação
        numero_de_clientes = 13

        for cliente_id in range(numero_de_clientes):
            ClienteModel.objects.create(
                first_name=f'Christian {cliente_id}',
                last_name=f'Surname {cliente_id}',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/api/clientes/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('clientes'))
        self.assertEqual(response.status_code, 200)

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('clientes'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['author_list']) == 10)

    def test_lists_all_authors(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('clientes')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['author_list']) == 3)