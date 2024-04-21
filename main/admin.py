from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']


class InlineProfile(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    fields = ['username', 'email']
    inlines = [InlineProfile]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
