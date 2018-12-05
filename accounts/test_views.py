from django.test import TestCase, Client
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import ProfilePicture

class TestAccountViews(TestCase):

    def test_get_register_page(self):
        response = self.client.get('/accounts/register/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('registration.html')
    

    def test_can_register_new_user_object(self):
        response = self.client.post('/accounts/register/', {'username': 'testuser999',
                                                            'email': 'testuser999@test.com',
                                                            'password1':'Helloworld',
                                                            'password2':'Helloworld'})
        user = get_object_or_404(User, username="testuser999")

        self.assertEqual(str(user), "testuser999")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/profile/')


    def test_same_username_can_not_be_reused(self):
        self.user = User.objects.create_user(username= 'testuser999',
                                        email= 'testuser999@test.com',
                                        password='Helloworld')
        self.user.save()

        response = self.client.post('/accounts/register/', {'username': 'testuser999',
                                                            'email': 'testuser999@test.com',
                                                            'password1':'Helloworld',
                                                            'password2':'Helloworld'})

        self.assertIn('A user with that username already exists.', str(response.content))


    def test_get_login_page(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('login.html')


    def test_can_login_with_user_credentials(self):
        #use create_user so that the password is properly hashed
        self.user = User.objects.create_user(username= 'testuser999',
                                        email= 'testuser999@test.com',
                                        password='Helloworld')
        self.user.save()

        response = self.client.get('/')
        self.assertEqual(str(response.wsgi_request.user), 'AnonymousUser')

        response2 = self.client.post('/accounts/login/', {'username': self.user.username,
                                                         'password':'Helloworld'})
        
        self.assertEqual(response2.status_code, 302)
        self.assertEqual(response2.url, '/')
        self.assertEqual(str(response2.wsgi_request.user), 'testuser999')
        self.assertEqual(response2.wsgi_request.user.is_authenticated, True)


    def test_wrong_login_credentials_fails_to_login_user(self):
        self.user = User.objects.create_user(username= 'testuser999',
                                        email= 'testuser999@test.com',
                                        password='Helloworld')
        self.user.save()
        response = self.client.post('/accounts/login/', {'username': self.user.username,
                                                         'password':'wrongpassword'})

        self.assertIn('Your username or password is incorrect!', str(response.content))


    def test_log_out_user(self):
        """Prove that the user is logged in with first response and that the user is logged out
           with the second response. """
        self.user = User.objects.create(username='admin',
                                         password='12345',)
        self.user.save()
        self.user.set_password("12345")
        self.user.save()

        self.client = Client()
        self.client.login(username='admin', password='12345')

        response = self.client.get('/')
        self.assertEqual(str(response.wsgi_request.user), 'admin')
        self.assertEqual(response.wsgi_request.user.is_authenticated, True)

        response2 = self.client.get('/accounts/logout/')
        #print(dir(response2))
        #print(response2.url)
        #print(response2.wsgi_request.user.is_authenticated)
        self.assertEqual(str(response2.wsgi_request.user), 'AnonymousUser')
        self.assertEqual(response2.wsgi_request.user.is_authenticated, False)

    def test_get_user_profile(self):
        self.user = User.objects.create(username='admin',
                                         password='12345',)
        self.user.save()
        self.user.set_password("12345")
        self.user.save()

        self.client = Client()
        self.client.login(username='admin', password='12345')

        response = self.client.get('/accounts/profile/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('profile.html')

    def test_set_profile_picture(self):
        self.user = User.objects.create(username='admin',
                                         password='12345',)

        self.user.save()
        self.user.set_password("12345")
        self.user.save()

        self.client = Client()
        self.client.login(username='admin', password='12345')

        response = self.client.post('/accounts/profile/', {'picture':'missing-profile-pic.png'})
        pic = get_object_or_404(ProfilePicture, user=self.user)

        self.assertEqual(str(pic), 'images/missing-profile-pic.png')

