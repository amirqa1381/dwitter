from django.urls import path
from .views import RegisterView, logout_view, Login, UpdateUserInfo

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('general-update/', UpdateUserInfo.as_view(), name='general_update_info')
]
