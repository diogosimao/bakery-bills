import copy
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.bills.serializers import BillSerializer, PaymentSerializer
from apps.branches.tests.test_models import create_branch, BRANCH_SAMPLE_TEST_DICT
from .test_models import create_bill, create_payment, BILL_SAMPLE_TEST_DICT


class CreateBillTest(APITestCase):
    def setUp(self):
        branch = create_branch(**BRANCH_SAMPLE_TEST_DICT)
        self.data = copy.deepcopy(BILL_SAMPLE_TEST_DICT)
        self.data['branch'] = branch.slug

    def test__api_create_bill(self):
        response = self.client.post(reverse('bills_api:bills_api-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadBillTest(APITestCase):
    def setUp(self):
        branch = create_branch(**BRANCH_SAMPLE_TEST_DICT)
        self.bill = create_bill(**BILL_SAMPLE_TEST_DICT, branch=branch)

    def test__api_read_bill_detail(self):
        response = self.client.get(reverse('bills_api:bills_api-detail', args=[self.bill.slug]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateBillTest(APITestCase):
    def setUp(self):
        branch = create_branch(**BRANCH_SAMPLE_TEST_DICT)
        self.bill = create_bill(**BILL_SAMPLE_TEST_DICT, branch=branch)
        self.data = BillSerializer(self.bill).data
        self.data.update({'description': 'Whole wheat 10 ounce bags'})

    def test__api_update_bill_detail(self):
        response = self.client.put(reverse('bills_api:bills_api-detail', args=[self.bill.slug]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteBillTest(APITestCase):
    def setUp(self):
        branch = create_branch(**BRANCH_SAMPLE_TEST_DICT)
        self.bill = create_bill(**BILL_SAMPLE_TEST_DICT, branch=branch)

    def test__api_delete_bill(self):
        response = self.client.delete(reverse('bills_api:bills_api-detail', args=[self.bill.slug]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreatePaymentTest(APITestCase):
    def setUp(self):
        branch = create_branch(**BRANCH_SAMPLE_TEST_DICT)
        self.data = BILL_SAMPLE_TEST_DICT
        self.bill = create_bill(**BILL_SAMPLE_TEST_DICT, branch=branch)
        self.data = {'payment_date': '2017-12-01', 'bill': self.bill.slug}

    def test__api_create_payment(self):
        response = self.client.post(reverse('bills_api:bill_api-payment-list', args=[self.bill.slug]), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadPaymentTest(APITestCase):
    def setUp(self):
        branch = create_branch(**BRANCH_SAMPLE_TEST_DICT)
        self.bill = create_bill(**BILL_SAMPLE_TEST_DICT, branch=branch)
        self.payment = create_payment(payment_date='2017-12-01', bill=self.bill)

    def test__api_read_payment_detail(self):
        response = self.client.get(reverse('bills_api:bill_api-payment-detail', args=[self.bill.slug, self.payment.slug]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdatePaymentTest(APITestCase):
    def setUp(self):
        branch = create_branch(**BRANCH_SAMPLE_TEST_DICT)
        self.bill = create_bill(**BILL_SAMPLE_TEST_DICT, branch=branch)
        self.payment = create_payment(payment_date='2017-12-01', bill=self.bill)
        self.data = PaymentSerializer(self.payment).data
        self.data.update({'due_date': '2000-12-12'})

    def test__api_update_payment_detail(self):
        response = self.client.put(reverse('bills_api:bill_api-payment-detail', args=[self.bill.slug, self.payment.slug]),
                                   self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeletePaymentTest(APITestCase):
    def setUp(self):
        branch = create_branch(**BRANCH_SAMPLE_TEST_DICT)
        self.bill = create_bill(**BILL_SAMPLE_TEST_DICT, branch=branch)
        self.payment = create_payment(payment_date='2017-12-01', bill=self.bill)

    def test__api_delete_payment(self):
        response = self.client.delete(reverse('bills_api:bill_api-payment-detail', args=[self.bill.slug, self.payment.slug]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

