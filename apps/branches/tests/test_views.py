from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CreateBranchTest(APITestCase):
    def setUp(self):
        self.data = {'description': '', 'address': 'Rua A', 'city': 'Barra Mansa', 'state': 'Rio de Janeiro'}

    def test_create_branch(self):
        response = self.client.post(reverse('branches:branches-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

