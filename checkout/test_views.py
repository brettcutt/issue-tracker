from django.test import TestCase, Client
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from accounts.models import ProfilePicture
from features.models import Features
from django.utils import timezone
from issuetracker import settings
import stripe
from datetime import datetime

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

        self.feature = Features.objects.create(name='test', description='this is a test', username=self.user)
        self.feature.save()

        c = Client()
        session = self.client.session
        session['cart'] = {str(self.feature.id): 1}
        session.save()
 
    def test_get_checkout_page(self):
        response = self.client.get('/checkout/')

        self.assertEqual(response.status_code, 200)

    """
    def test_make_a_successful_payment_and_redirect_to_feature_upvote(self):
        stripe.api_key = settings.STRIPE_SECRET

        token = stripe.Token.create(
            card={
                'number': '4242424242424242',
                'exp_month': '6',
                'exp_year': str(datetime.today().year + 1),
                'cvc': '111',
            }
        )
        response = self.client.post('/checkout/',{'stripe_id':token.id})
        #print()
        #print(dir(response))
        #print('')
        #print(response._headers)
        #print('')
        #print(response.wsgi_request)
        #print('')
        #print(response.url)
        self.assertNotIn("We were unable to take a payment with that card!",str(response.content))
        self.assertNotIn("Your card was declined!",str(response.content))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/features/upvote_feature/')
        print(response.content) """

    def test_make_sure_a_unsuccessful_payment_returns_error_message(self):
        
        response = self.client.post('/checkout/',{'number': '4242424242424248',
                'exp_month': '12',
                'exp_year': '2018',
                'cvc': '111',})

        self.assertIn("We were unable to take a payment with that card!",str(response.content))