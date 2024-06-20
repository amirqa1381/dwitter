from django.urls import path
from .views import UserInformationAndJobDetailsView


urlpatterns = [
    path('info-detail/', UserInformationAndJobDetailsView.as_view(), name='user_information'),
]