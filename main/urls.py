from django.urls import path
from .views import profile_list, profile_detail, dashboard

urlpatterns = [
    # path('', index_page, name='index'),
    path('profile-list/', profile_list, name='profile_list'),
    path('profile-detail/<int:profile_id>/', profile_detail, name='profile_detail'),
    path('', dashboard, name='dashboard'),
]
