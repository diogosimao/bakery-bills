import copy
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.bills.serializers import BillSerializer
from apps.branches.tests.test_models import create_branch, BRANCH_SAMPLE_TEST_DICT
from .test_models import create_bill, BILL_SAMPLE_TEST_DICT


class CreateBillTest(APITestCase):
    def setUp(self):
        branch = create_branch(**BRANCH_SAMPLE_TEST_DICT)
        self.data = copy.deepcopy(BILL_SAMPLE_TEST_DICT)
        self.data['branch'] = branch.id

    def test__create_bill(self):
        response = self.client.post(reverse('bills:bills-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadBillTest(APITestCase):
    def setUp(self):
        branch = create_branch(**BRANCH_SAMPLE_TEST_DICT)
        self.bill = create_bill(**BILL_SAMPLE_TEST_DICT, branch=branch)

    def test__read_bill_detail(self):
        response = self.client.get(reverse('bills:bills-detail', args=[self.bill.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateBillTest(APITestCase):
    def setUp(self):
        branch = create_branch(**BRANCH_SAMPLE_TEST_DICT)
        self.bill = create_bill(**BILL_SAMPLE_TEST_DICT, branch=branch)
        self.data = BillSerializer(self.bill).data
        self.data.update({'description': 'Whole wheat 10 ounce bags'})

    def test__update_bill_detail(self):
        response = self.client.put(reverse('bills:bills-detail', args=[self.bill.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteBillTest(APITestCase):
    def setUp(self):
        branch = create_branch(**BRANCH_SAMPLE_TEST_DICT)
        self.bill = create_bill(**BILL_SAMPLE_TEST_DICT, branch=branch)

    def test__delete_bill(self):
        response = self.client.delete(reverse('bills:bills-detail', args=[self.bill.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

