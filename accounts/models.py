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
    answered = models.BooleanField(default=False, verbose_name='Answered', null=True, blank=True)

    def __str__(self):
        return self.subject


class AnswersForContact(models.Model):
    """
    This function is for answers for contact messages
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name='Contact')
    answer = models.TextField(verbose_name='Answer')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Updated at')

    def __str__(self):
        return f"{self.user.username} -> {self.answer[:20]} ...."