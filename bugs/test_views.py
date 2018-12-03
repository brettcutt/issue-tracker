from django.test import TestCase, Client
from django.shortcuts import get_object_or_404
from .models import Bugs, Comments
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

        self.bug = Bugs.objects.create(name='test', description='this is a test', username=self.user)
        self.bug.save()
        

        #self.client.force_login(self.user)  #can use this to login with out password
    
    def test_get_bugs_page(self):
        response = self.client.get('/bugs/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bugs.html')

    def test_get_bug_detail_page(self):
        response = self.client.get('/bugs/bug_detail/{0}/'.format(self.bug.id))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bug_detail.html')

    def test_add_bug_page(self):

        response = self.client.get("/bugs/add_bug/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_ticket.html')

    def test_add_a_new_bug(self):
        response = self.client.post('/bugs/add_bug/',
         {'name':'new bug',
          'description': 'this is the description',
          'username': self.user,
          'created_date':timezone.now,
          'views': 0,
          'upvotes': 0,
          'picture': self.pic,
          'status':'Waiting' })
        item = get_object_or_404(Bugs, pk=1)
        self.assertEqual(item.username, self.user)
        self.assertEqual(response.status_code, 302)

    def test_edit_bug_page(self):
        response = self.client.get("/bugs/edit_bug/{0}/".format(self.bug.id))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_ticket.html')
    
    def test_edit_a_bug(self):
        response = self.client.post('/bugs/edit_bug/{0}/'.format(self.bug.id),
         {'name':'edited bug',
          'description': 'this is the description',
          'username': self.user,
          'created_date':timezone.now,
          'views': 0,
          'upvotes': 0,
          'picture': self.pic,
          'status':'In Progress' })
        item = get_object_or_404(Bugs, pk=1)
        self.assertEqual(item.username, self.user)
        self.assertEqual(response.status_code, 302)






    def test_get_edit_page_for_item_that_does_not_exist(self):
        response = self.client.get('/bugs/edit_bug/99/')
        self.assertEqual(response.status_code, 404)

    def test_get_upvote_bug(self):
        response = self.client.get('/bugs/upvote_bug/{0}/'.format(self.bug.id))
        self.assertEqual(response.status_code, 302)

    def test_post_create_a_new_comment(self):
        response = self.client.post('/bugs/add_comment_bugs/{0}/'.format(self.bug.id),
         {'ticket':self.bug,
          'username': self.user,
          'picture': self.pic,
          'created_date':timezone.now,
          'comment':"this is a comment"})
        item = get_object_or_404(Comments, pk=1)
        self.assertEqual(item.username, self.user)
        self.assertEqual(response.status_code, 302)