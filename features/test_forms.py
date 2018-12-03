from django.test import TestCase
from .views import FeaturesForm


class TestFeaturesForm(TestCase):

    def test_can_create_a_ticket_with_just_a_name(self):
        form = FeaturesForm({'name': 'New Feature'})
        self.assertTrue(form.is_valid)

    def test_correct_message_for_missing_name(self):
        form = FeaturesForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])
