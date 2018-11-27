from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from accounts.models import ProfilePicture


class Bugs(models.Model):
    TODO = 'To Do'
    DOING = 'Doing'
    DONE = 'Done'
    STATUS_CHOICES = ((TODO, 'To do'), (DOING, 'Doing'), (DONE, 'Done'))

    name = models.CharField(max_length=40, blank=False)
    description = models.TextField(blank=False)
    username = models.ForeignKey(User, default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    picture = models.ForeignKey(ProfilePicture, null=True)
    status = models.CharField(
        max_length=40, choices=STATUS_CHOICES, default=TODO)

    def __str__(self):
        return self.name


class Features(models.Model):
    TODO = 'To Do'
    DOING = 'Doing'
    DONE = 'Done'
    STATUS_CHOICES = ((TODO, 'To do'), (DOING, 'Doing'), (DONE, 'Done'))

    name = models.CharField(max_length=40, blank=False)
    description = models.TextField(blank=False)
    username = models.ForeignKey(User, default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    picture = models.ForeignKey(ProfilePicture, null=True)
    status = models.CharField(
        max_length=40, choices=STATUS_CHOICES, default=TODO)

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
