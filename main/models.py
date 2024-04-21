from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', related_name='profile')
    image = models.ImageField(upload_to='profile_pics/', verbose_name='Image', blank=True)
    follows = models.ManyToManyField('self', related_name='followers', symmetrical=False, blank=True)

    def __str__(self):
        return str(self.user.username)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
        profile.follows.add(instance.profile)
        profile.save()
