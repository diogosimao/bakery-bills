from django.test import TestCase

from apps.branches.models import Branch


BRANCH_SAMPLE_TEST_DICT = {'description': 'Matriz', 'address': 'Rua A', 'city': 'Barra Mansa',
                           'state': 'Rio de Janeiro'}


def create_branch(**kwargs):
    branch = Branch(**kwargs)
    branch.save()
    return branch


class BranchModelTestCase(TestCase):

    def setUp(self):
        self.old_count = Branch.objects.count()
        self.branch = create_branch(**BRANCH_SAMPLE_TEST_DICT)

    def test__model_can_create_branch(self):
        self.assertNotEqual(self.old_count, Branch.objects.count())
        self.assertTrue(isinstance(self.branch, Branch))

    def test__model_can_return_branch_description(self):
        self.assertEqual(self.branch.__str__(), 'Matriz')

