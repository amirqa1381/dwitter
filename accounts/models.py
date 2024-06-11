from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    """
    this model is for store the contact messages of the user that , user talk to us,
    and we store the user messages for better helping to user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    subject = models.CharField(max_length=100, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    answered = models.BooleanField(default=False, verbose_name='Answered')

    def __str__(self):
        return self.subject
