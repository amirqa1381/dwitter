from django.shortcuts import render
from .models import Room, Message
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required


@login_required
def rooms(request: HttpRequest):
    """
    this function is for handling the rooms view and showing the all rooms to the user
    """
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'room/rooms.html', context)


@login_required
def room(request: HttpRequest, slug):
    """
    This is the function for handling the room page and showing the chat of that to the user
    """
    room = Room.objects.get(slug=slug)
    contents = Message.objects.filter(room=room)[:25]
    context = {
        'room': room,
        'contents': contents
    }
    return render(request, 'room/room.html', context)
