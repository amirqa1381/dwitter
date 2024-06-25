from django.urls import path
from .views import UserInformationAndJobDetailsView, CreatProductView, ProductListView, ProductDetailView


urlpatterns = [
    path('', ProductListView.as_view(), name='store_page'),
    path('detail/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('info-detail/', UserInformationAndJobDetailsView.as_view(), name='user_information'),
    path('insert-product/', CreatProductView.as_view(), name='create_product'),
]