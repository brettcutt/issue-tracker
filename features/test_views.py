from django.test import TestCase, Client
from django.shortcuts import get_object_or_404
from .models import Features, UpvoteFeature
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

        self.feature = Features.objects.create(name='feature title', description='this is a description', username=self.user)
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

    def test_get_add_feature_page(self):

        response = self.client.get("/features/add_feature/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_ticket.html')

    def test_adding_a_new_feature(self):
        response = self.client.post('/features/add_feature/',
         {'name':'feature title',
          'description': 'this is a description',
          'username': self.user,
          'created_date':timezone.now,
          'views': 0,
          'upvotes': 0,
          'status':'Waiting' })
        item = get_object_or_404(Features, pk=1)
        self.assertEqual(item.name, 'feature title')
        self.assertEqual(item.description, 'this is a description')
        self.assertEqual(str(item.username), 'admin')
        self.assertEqual(item.views, 0)
        self.assertEqual(item.upvotes, 0)
        self.assertEqual(item.status, 'Waiting')
        self.assertEqual(response.status_code, 302)

    def test_edit_feature_page(self):
        response = self.client.get("/features/edit_feature/{0}/".format(self.feature.id))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_ticket.html')
    
    def test_edit_a_feature_ticket(self):
        response = self.client.post('/features/edit_feature/{0}/'.format(self.feature.id),
         {'name':'edited feature',
          'description': 'this is the new description',
          'username': self.user,
          'created_date':timezone.now,
          'views': 0,
          'upvotes': 0,
          'status':'In Progress' })
        item = get_object_or_404(Features, pk=1)
        self.assertEqual(item.name, 'edited feature')
        self.assertEqual(item.description, 'this is the new description')
        self.assertEqual(str(item.username), 'admin')
        self.assertEqual(item.views, -1)
        self.assertEqual(item.upvotes, 0)
        self.assertEqual(item.status, 'In Progress')
        self.assertEqual(response.status_code, 302)

    def test_get_edit_page_for_item_that_does_not_exist(self):
        response = self.client.get('/features/edit_bug/99/')
        self.assertEqual(response.status_code, 404)

    def test_post_create_a_new_feature_comment(self):
        response = self.client.post('/features/add_comment_features/{0}/'.format(self.feature.id),
         {'feature_ticket':self.feature,
          'username': self.user,
          'picture': self.pic,
          'created_date':timezone.now,
          'comment':"this is a comment"})

        comment_object = get_object_or_404(Comments, pk=1)

        self.assertEqual(str(comment_object.feature_ticket), "feature title")
        self.assertEqual(str(comment_object.username), "admin")
        self.assertEqual(str(comment_object.picture), "missing-profile-pic.png")
        self.assertEqual(comment_object.comment, "this is a comment")
        self.assertEqual(response.status_code, 302)

    def test_get_upvote_feature(self):
        response = self.client.get('/features/upvote_feature/')
        #print(dir(response))
        #print('1; ', response.has_header)
        self.assertEqual(response.status_code, 302)

    def test_create_upvote_object_and_send_one_upvote_to_feature_object(self):
        
        c = Client()
        session = self.client.session
        session['cart'] = {str(self.feature.id): 1}
        session.save()

        response = self.client.get('/features/upvote_feature/')

        upvote_object = get_object_or_404(UpvoteFeature, upvoted_feature=self.feature)
        feature_point = get_object_or_404(Features, name=upvote_object.upvoted_feature)

        self.assertEqual(str(upvote_object.user), 'admin')
        self.assertEqual(str(upvote_object.upvoted_feature), 'feature title')

        self.assertEqual(int(feature_point.upvotes), 1)


    