from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ProfilePicture(models.Model):
    picture = models.ImageField(
        upload_to='images', blank=True)
    user = models.ForeignKey(User, default=None)

    def __str__(self):
        return str(self.picture)
