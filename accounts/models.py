from django.db import models

# Create your models here.


class ProfilePicture(models.Model):
    picture = models.ImageField(
        upload_to='images', blank=True)
    user = models.CharField(max_length=40, blank=False)

    def __str__(self):
        return str(self.picture)
