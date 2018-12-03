from django.test import TestCase
from .views import UserLoginForm, UserRegistrationForm, ProfilePicForm


class TestLoginForm(TestCase):

    def test_login_form_is_valid(self):
        form = UserLoginForm(
            {'username': 'test3@test.com', 'password': 'testpassword'})

        self.assertTrue(form.is_valid())

    def test_correct_message_for_missing_name(self):
        form = UserLoginForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])


class TestRegistrationForm(TestCase):
    def test_register_form_is_valid(self):

        form = UserRegistrationForm({'email': 'test@test.com', 'username': 'testuser',
                                     'password1': 'testpassword', 'password2': 'testpassword'})

        self.assertTrue(form.is_valid())


class TestProfilePictureForm(TestCase):
    def test_profile_pic_form_is_valid(self):
        form = ProfilePicForm({'picture': 'hello'})
        self.assertTrue(form.is_valid())
