from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.branches.serializers import BranchSerializer
from .test_models import create_branch, SAMPLE_TEST_DICT


class CreateBranchTest(APITestCase):
    def setUp(self):
        self.data = SAMPLE_TEST_DICT

    def test_create_branch(self):
        response = self.client.post(reverse('branches:branches-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadBranchTest(APITestCase):
    def setUp(self):
        self.branch = create_branch(**SAMPLE_TEST_DICT)

    def test_read_branch_list(self):
        response = self.client.get(reverse('branches:branches-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_branch_detail(self):
        response = self.client.get(reverse('branches:branches-detail', args=[self.branch.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateBranchTest(APITestCase):
    def setUp(self):
        self.branch = create_branch(**SAMPLE_TEST_DICT)
        self.data = BranchSerializer(self.branch).data
        self.data.update({'description': 'Loja principal'})

    def test_update_branch(self):
        response = self.client.put(reverse('branches:branches-detail', args=[self.branch.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteBranchTest(APITestCase):
    def setUp(self):
        self.branch = create_branch(**SAMPLE_TEST_DICT)

    def test_delete_branch(self):
        response = self.client.delete(reverse('branches:branches-detail', args=[self.branch.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

