from django.db import models
from django.contrib.auth.models import User
from features.models import Features


class Upvote(models.Model):
    upvoted_feature = models.ForeignKey(Features, default=None)
    user = models.ForeignKey(User, default=None)

    def __str__(self):
        return str(self.user)
