#from django.test import TestCase
#from .views import BugsForm
#
#
#class TestBugsForm(TestCase):
#
#    def test_can_create_a_ticket_with_just_a_name(self):
#        form = BugsForm({'name': 'New Bug'})
#        self.assertTrue(form.is_valid)
#
#    def test_correct_message_for_missing_name(self):
#        form = BugsForm({'name': ''})
#        self.assertFalse(form.is_valid())
#        self.assertEqual(form.errors['name'], [u'This field is required.'])
#