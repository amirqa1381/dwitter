from django.urls import path
from .views import UserInformationAndJobDetailsView, create_product


urlpatterns = [
    path('info-detail/', UserInformationAndJobDetailsView.as_view(), name='user_information'),
    path('insert-product/', create_product, name='insert_product')
]