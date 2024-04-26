from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']


class InlineProfile(admin.StackedInline):
    model = Profile


class AdminUser(UserAdmin):
    list_display = ['username', 'email']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Date', {'fields': ('last_login', 'date_joined')}),
    )
    inlines = [InlineProfile]


admin.site.unregister(User)
admin.site.register(User, AdminUser)
admin.site.unregister(Group)
