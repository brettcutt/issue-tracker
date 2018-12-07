from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from features.models import Features
from accounts.models import ProfilePicture


class Bugs(models.Model):
    WAITING = 'Waiting'
    INPROGRESS = 'In Progress'
    COMPLETED = 'Completed'
    STATUS_CHOICES = ((WAITING, 'Waiting'),
                      (INPROGRESS, 'In Progress'), (COMPLETED, 'Completed'))

    name = models.CharField(max_length=28, blank=False)
    description = models.TextField(blank=False)
    username = models.ForeignKey(User, default=None)
    created_date = models.DateTimeField(blank=True, default=None, null=True)
    waiting_date = models.DateTimeField(blank=True, default=None, null=True)
    in_progress_date = models.DateTimeField(
        blank=True, default=None, null=True)
    completion_date = models.DateTimeField(blank=True, default=None, null=True)
    views = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    picture = models.ForeignKey(ProfilePicture, null=True)
    status = models.CharField(
        max_length=40, choices=STATUS_CHOICES, default=WAITING)

    def __str__(self):
        return self.name


class Comments(models.Model):
    ticket = models.ForeignKey(Bugs, null=True)
    feature_ticket = models.ForeignKey(Features, null=True)
    username = models.ForeignKey(User, null=None)
    comment = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    picture = models.ForeignKey(ProfilePicture, null=True)

    def __str__(self):
        return self.comment


class BugUpvote(models.Model):
    upvoted_bug = models.ForeignKey(Bugs, default=None)
    user = models.ForeignKey(User, default=None)

    def __str__(self):
        return str(self.user)
