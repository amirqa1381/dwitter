from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', related_name='profile')
    image = models.ImageField(upload_to='profile_pics/', verbose_name='Image', blank=True)
    follows = models.ManyToManyField('self', related_name='followers', symmetrical=False, blank=True)

    def __str__(self):
        return str(self.user.username)
