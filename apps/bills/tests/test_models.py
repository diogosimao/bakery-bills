from datetime import datetime
from django.test import TestCase

from apps.bills.models import Bill, Payment
from apps.branches.tests.test_models import create_branch, BRANCH_SAMPLE_TEST_DICT


BILL_SAMPLE_TEST_DICT = {'description': 'Whole wheat', 'debit': '90.00', 'due_date': datetime.date(datetime.now())}


def create_bill(**kwargs):
    bill = Bill(**kwargs)
    bill.save()
    return bill


def create_payment(**kwargs):
    payment = Payment(**kwargs)
    payment.save()
    return payment


class BillModelTestCase(TestCase):

    def setUp(self):
        self.old_count = Bill.objects.count()
        self.branch = create_branch(**BRANCH_SAMPLE_TEST_DICT)
        self.bill = create_bill(**BILL_SAMPLE_TEST_DICT, branch=self.branch)

    def test__model_can_create_bill(self):
        self.assertNotEqual(self.old_count, Bill.objects.count())
        self.assertTrue(isinstance(self.bill, Bill))
        self.assertTrue(self.bill.branch == self.branch)

    def test__model_can_return_bill_description(self):
        self.assertEqual(self.bill.__str__(), 'Whole wheat')


class PaymentModelTestCase(TestCase):

    def setUp(self):
        self.branch = create_branch(**BRANCH_SAMPLE_TEST_DICT)
        self.branch.save()
        self.bill = create_bill(**BILL_SAMPLE_TEST_DICT, branch=self.branch)
        self.bill.save()
        self.old_count = Payment.objects.count()
        self.payment = create_payment(payment_date='2017-12-01', bill=self.bill)

    def test__model_can_create_payment(self):
        self.assertNotEqual(self.old_count, Payment.objects.count())
        self.assertTrue(isinstance(self.payment, Payment))

    def test__model_can_return_payment_str(self):
        self.assertEqual(self.payment.__str__(), '2017-12-01')

