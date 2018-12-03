from django.test import TestCase, Client
from features.models import Features
from .models import Upvote
from django.contrib.auth.models import User

class TestUpvote(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='testuser',
                                         password='12345', 
                                         is_active=True, 
                                         is_staff=True, 
                                         is_superuser=True)
        self.user.set_password("12345")
        self.user.save()
        print(self.user)

        self.client = Client()
        self.client.login(username='testuser', password='12345')

        self.feature = Features.objects.create(name='test', description='this is a test', username=self.user)
        self.feature.save()
    def test_upvote_form(self):
        upvote = Upvote.objects.create(upvoted_feature=self.feature,
                                       user=self.user)
        self.assertEqual(str(upvote.upvoted_feature), 'test')
        self.assertEqual(str(upvote.user), "testuser")