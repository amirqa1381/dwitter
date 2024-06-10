from django.urls import path
from .views import rooms, room, CreateRoomChating, DeleteRoomView

urlpatterns = [
    path('', rooms, name='rooms'),
    path('create-room/', CreateRoomChating.as_view(), name='create_room-chating'),
    path('<slug:slug>/', room, name='room'),
    path('<slug:slug>/delete/', DeleteRoomView.as_view(), name='delete_room'),
]
