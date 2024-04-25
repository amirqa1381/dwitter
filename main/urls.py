from django.urls import path
from .views import index_page, profile_list, profile_detail

urlpatterns = [
    path('', index_page, name='index'),
    path('profile-list/', profile_list, name='profile_list'),
    path('profile-detail/<int:profile_id>/', profile_detail, name='profile_detail'),
]
