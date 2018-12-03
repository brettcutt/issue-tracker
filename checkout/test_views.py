from django.test import TestCase, Client
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from accounts.models import ProfilePicture
from django.utils import timezone

#class TestViews(TestCase):
#    def setUp(self):
#        self.user = User.objects.create(username='admin',
#                                         password='12345', 
#                                         is_active=True, 
#                                         is_staff=True, 
#                                         is_superuser=True)
#        self.user.set_password("12345")
#        self.user.save()
#
#        self.pic = ProfilePicture.objects.create(picture='missing-profile-pic.png', user=self.user)
#        self.pic.save()
#
#        self.client = Client()
#        self.client.login(username='admin', password='12345')
#
#        self.bug = Bugs.objects.create(name='test', description='this is a test', username=self.user)
#        self.bug.save()
# 