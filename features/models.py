from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from accounts.models import ProfilePicture


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
