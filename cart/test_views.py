from django.test import TestCase, Client
from django.shortcuts import get_object_or_404
from features.models import Features
from bugs.forms import CommentForm
from django.contrib.auth.models import User
from accounts.models import ProfilePicture
from django.utils import timezone

class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='admin',
                                         password='12345', 
                                         is_active=True, 
                                         is_staff=True, 
                                         is_superuser=True)
        self.user.set_password("12345")
        self.user.save()

        self.pic = ProfilePicture.objects.create(picture='missing-profile-pic.png', user=self.user)
        self.pic.save()

        self.client = Client()
        self.client.login(username='admin', password='12345')

        self.feature = Features.objects.create(name='feature title', description='this is a description', username=self.user)
        self.feature.save()

        c = Client()
        session = self.client.session
        session['cart'] = {str(self.feature.id): 1}
        session.save()

    def test_get_cart_page(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')

    def test_feature_in_cart_is_displayed_on_cart_page(self):
        response = self.client.get('/cart/')
        self.assertIn('feature title', str(response.content))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')

    def test_add_new_feature_to_cart(self):
        self.feature2 = Features.objects.create(name='new feature', description='this is a description', username=self.user, picture=self.pic)
        self.feature2.save()

        response = self.client.post('/cart/add/{0}/'.format(self.feature2.id), {'quantity': 1})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/features/feature_detail/2/')



    def test_feature_can_be_removed_from_the_cart(self):
        response = self.client.post('/cart/remove_ticket/{0}/'.format(self.feature.id), {'quantity': 0})
        self.assertNotIn('feature title', str(response.content))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/cart/')