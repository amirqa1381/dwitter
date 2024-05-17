from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', related_name='profile')
    image = models.ImageField(upload_to='profile_pics/', verbose_name='Image')
    follows = models.ManyToManyField('self', related_name='followers', symmetrical=False, blank=True)

    def __str__(self):
        return str(self.user.username)


class Dweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    content = models.CharField(max_length=300, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    dweet_file = models.FileField(upload_to='dweet_file/', verbose_name="Dweet File", null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Is Active')

    # class Meta:
    #     ordering = ['-created_at']

    def __str__(self):
        return f"""
        {self.user.username} /
        {self.created_at:"%Y-%m-%d %H:%M:%S"} / 
        {self.content[:20]} ...
        """


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
        profile.follows.add(instance.profile)
        profile.save()
