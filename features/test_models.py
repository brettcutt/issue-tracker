from django.test import TestCase, Client
from bugs.models import Comments
from .models import Features
from django.contrib.auth.models import User
from accounts.models import ProfilePicture
from django.utils import timezone

class TestBugModels(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='testuser',
                                         password='12345', 
                                         is_active=True, 
                                         is_staff=True, 
                                         is_superuser=True)
        self.user.set_password("12345")
        self.user.save()
        print(self.user)

        self.pic = ProfilePicture.objects.create(picture='missing-profile-pic.png', user=self.user)
        self.pic.save()

        self.client = Client()
        self.client.login(username='testuser', password='12345')

        self.feature = Features.objects.create(name='test', description='this is a test', username=self.user)

    def test_features_form(self):
        pic = ProfilePicture.objects.get(user=self.user)
        
        feature = Features.objects.create(name="Test feature Form", 
                                  description='This is a test', 
                                  username=self.user,
                                  picture=pic)
        feature.save()
        
        self.assertEqual(feature.name, 'Test feature Form')
        self.assertEqual(feature.description, 'This is a test')
        self.assertEqual(str(feature.username), 'testuser')
        self.assertEqual(feature.status, 'Waiting')
        self.assertEqual(str(feature.picture), 'missing-profile-pic.png')
        self.assertEqual(feature.views, 0)
        self.assertEqual(feature.upvotes, 0)


    def test_comments_form(self):
        feature = Features.objects.get(id=self.feature.id)
        pic = ProfilePicture.objects.get(user=self.user)
        comment = Comments.objects.create(ticket=None, 
                                          feature_ticket=feature, 
                                          username=self.user,
                                          picture=pic,
                                          comment="This is the comment",
                                          )
        self.assertEqual(str(comment.username), 'testuser')
        self.assertEqual(comment.ticket, None)
        self.assertEqual(str(comment.feature_ticket), 'test')
        self.assertEqual(str(comment.picture), 'missing-profile-pic.png')
        self.assertEqual(comment.comment, "This is the comment")

    
#    def test_bug_upvote_form(self):
#        bug = Bugs.objects.get(id=self.bug.id)
#
#        upvote = BugUpvote.objects.create(upvoted_bug=bug,
#                                          user=self.user)
#
#        self.assertEqual(str(upvote.user), str('testuser'))
#        self.assertEqual(str(upvote.upvoted_bug), 'test')
#
#
#