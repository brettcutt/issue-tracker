from django.test import TestCase, Client
from django.shortcuts import get_object_or_404
from .models import Features
from bugs.models import Comments
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

        self.feature = Features.objects.create(name='test', description='this is a test', username=self.user)
        self.feature.save()
        

        #self.client.force_login(self.user)  #can use this to login with out password
    
    def test_get_features_page(self):
        response = self.client.get('/features/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'features.html')

    def test_get_feature_detail_page(self):
        response = self.client.get('/features/feature_detail/{0}/'.format(self.feature.id))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feature_detail.html')

    def test_add_feature_page(self):

        response = self.client.get("/features/add_feature/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_ticket.html')

    def test_add_a_new_feature(self):
        response = self.client.post('/features/add_feature/',
         {'name':'new feature',
          'description': 'this is the description',
          'username': self.user,
          'created_date':timezone.now,
          'views': 0,
          'upvotes': 0,
          'picture': self.pic,
          'status':'Waiting' })
        item = get_object_or_404(Features, pk=1)
        self.assertEqual(item.username, self.user)
        self.assertEqual(response.status_code, 302)

    def test_edit_feature_page(self):
        response = self.client.get("/features/edit_feature/{0}/".format(self.feature.id))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_ticket.html')
    
    def test_edit_a_feature_ticket(self):
        response = self.client.post('/features/edit_feature/{0}/'.format(self.feature.id),
         {'name':'edited feature',
          'description': 'this is the description',
          'username': self.user,
          'created_date':timezone.now,
          'views': 0,
          'upvotes': 0,
          'picture': self.pic,
          'status':'In Progress' })
        item = get_object_or_404(Features, pk=1)
        self.assertEqual(item.username, self.user)
        self.assertEqual(response.status_code, 302)

    def test_get_edit_page_for_item_that_does_not_exist(self):
        response = self.client.get('/features/edit_bug/99/')
        self.assertEqual(response.status_code, 404)

    def test_post_create_a_new__feature_comment(self):
        response = self.client.post('/features/add_comment_features/{0}/'.format(self.feature.id),
         {'feature_ticket':self.feature,
          'username': self.user,
          'picture': self.pic,
          'created_date':timezone.now,
          'comment':"this is a comment"})
        item = get_object_or_404(Comments, pk=1)
        self.assertEqual(item.username, self.user)
        self.assertEqual(response.status_code, 302)