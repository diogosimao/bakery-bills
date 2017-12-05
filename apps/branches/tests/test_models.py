from django.test import TestCase

from apps.branches.models import Branch


SAMPLE_TEST_DICT = {'description': 'Matriz', 'address': 'Rua A', 'city': 'Barra Mansa', 'state': 'Rio de Janeiro'}


def create_branch(**kwargs):
    return Branch(**kwargs)


class BranchModelTestCase(TestCase):

    def setUp(self):
        self.branch = create_branch(**SAMPLE_TEST_DICT)

    def test__model_can_create_branch(self):
        old_count = Branch.objects.count()
        self.branch.save()
        new_count = Branch.objects.count()
        self.assertNotEqual(old_count, new_count)
        self.assertTrue(isinstance(self.branch, Branch))

    def test__model_can_return_branch_description(self):
        self.assertEqual(self.branch.__str__(), 'Matriz')

