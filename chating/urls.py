from django.urls import path
from .views import rooms_view, room_detail_view

urlpatterns = [
    path('', rooms_view, name='chating'),
    path('room/<slug:room_slug>/', room_detail_view, name='room_detail_view'),
]