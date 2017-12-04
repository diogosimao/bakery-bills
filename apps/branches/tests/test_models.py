from django.test import TestCase

from apps.branches.models import Branch


def create_branch(**kwargs):
    return Branch(**kwargs)


class BranchModelTestCase(TestCase):

    def setUp(self):
        self.branch = create_branch(description='Matrix', address='Rua A', city='Barra Mansa', state='Rio de Janeiro')

    def test__model_can_create_branch(self):
        old_count = Branch.objects.count()
        self.branch.save()
        new_count = Branch.objects.count()
        self.assertNotEqual(old_count, new_count)
        self.assertTrue(isinstance(self.branch, Branch))

    def test__model_can_return_branch_description(self):
        self.assertEqual(self.branch.__str__(), 'Matrix')

    def test__model_can_not_return_branch_description(self):
        branch = create_branch(address='Rua A', city='Barra Mansa', state='Rio de Janeiro')
        branch.save()
        self.assertEqual(branch.__str__(), 'Rua A')

