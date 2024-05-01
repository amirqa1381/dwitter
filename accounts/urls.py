from django.urls import path
from .views import RegisterView, logout_view, Login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]
