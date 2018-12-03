from django.test import TestCase, Client
from .models import Bugs, Comments, BugUpvote
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

        self.bug = Bugs.objects.create(name='test', description='this is a test', username=self.user)

    def test_bugs_form(self):
        pic = ProfilePicture.objects.get(user=self.user)
        
        bug = Bugs.objects.create(name="Test Bug Form", 
                                  description='This is a test', 
                                  username=self.user,
                                  picture=pic)
        bug.save()
        print('1.', bug.username)
        self.assertEqual(bug.name, 'Test Bug Form')
        self.assertEqual(bug.description, 'This is a test')
        self.assertEqual(str(bug.username), 'testuser')
        self.assertEqual(bug.status, 'Waiting')
        self.assertEqual(str(bug.picture), 'missing-profile-pic.png')
        self.assertEqual(bug.views, 0)
        self.assertEqual(bug.upvotes, 0)


    def test_comments_form(self):
        bug = Bugs.objects.get(id=self.bug.id)
        pic = ProfilePicture.objects.get(user=self.user)
        comment = Comments.objects.create(ticket=bug, 
                                          feature_ticket=None, 
                                          username=self.user,
                                          picture=pic,
                                          comment="This is the comment",
                                          )
        self.assertEqual(str(comment.username), 'testuser')
        self.assertEqual(str(comment.ticket), 'test')
        self.assertEqual(comment.feature_ticket, None)
        self.assertEqual(str(comment.picture), 'missing-profile-pic.png')
        self.assertEqual(comment.comment, "This is the comment")

    
    def test_bug_upvote_form(self):
        bug = Bugs.objects.get(id=self.bug.id)

        upvote = BugUpvote.objects.create(upvoted_bug=bug,
                                          user=self.user)

        self.assertEqual(str(upvote.user), str('testuser'))
        self.assertEqual(str(upvote.upvoted_bug), 'test')


