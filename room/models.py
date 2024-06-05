from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Room(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Room', related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', related_name='messages')
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date')

    class Meta:
        ordering = ('date',)
