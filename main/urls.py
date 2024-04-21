from django.urls import path
from .views import index_page, profile_list

urlpatterns = [
    path('', index_page, name='index'),
    path('profile-list/', profile_list, name='profile_list')
]
