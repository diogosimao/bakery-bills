from datetime import datetime
from django.test import TestCase

from apps.bills.models import Bill, Payment
from apps.branches.tests.test_models import create_branch, SAMPLE_TEST_DICT


def create_bill(**kwargs):
    return Bill(**kwargs)


def create_payment(**kwargs):
    return Payment(**kwargs)


class BillModelTestCase(TestCase):

    def setUp(self):
        self.branch = create_branch(**SAMPLE_TEST_DICT)
        self.branch.save()
        self.bill = create_bill(description='Whole wheat', debit=90.00, due_date=datetime.now(), branch=self.branch)

    def test__model_can_create_bill(self):
        old_count = Bill.objects.count()
        self.bill.save()
        new_count = Bill.objects.count()
        self.assertNotEqual(old_count, new_count)
        self.assertTrue(isinstance(self.bill, Bill))

    def test__model_can_return_bill_description(self):
        self.assertEqual(self.bill.__str__(), 'Whole wheat')


class PaymentModelTestCase(TestCase):

    def setUp(self):
        self.branch = create_branch(**SAMPLE_TEST_DICT)
        self.branch.save()
        self.bill = create_bill(description='Whole wheat', debit=90.00, due_date=datetime.now(), branch=self.branch)
        self.bill.save()
        self.payment = create_payment(payment_date='2017-12-01', bill=self.bill)

    def test__model_can_create_payment(self):
        old_count = Payment.objects.count()
        self.payment.save()
        new_count = Payment.objects.count()
        self.assertNotEqual(old_count, new_count)
        self.assertTrue(isinstance(self.payment, Payment))

    def test__model_can_return_payment_str(self):
        self.assertEqual(self.payment.__str__(), '2017-12-01')

