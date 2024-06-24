from django.urls import path
from .views import UserInformationAndJobDetailsView, CreatProductView


urlpatterns = [
    path('info-detail/', UserInformationAndJobDetailsView.as_view(), name='user_information'),
    path('insert-product/', CreatProductView.as_view(), name='create_product')
]