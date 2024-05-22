from django.shortcuts import render
from .models import Room
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest


@login_required
def rooms_view(request: HttpRequest):
    """
    this function is for showing rooms in the template
    """
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'chating/chating_room.html', context)


@login_required
def room_detail_view(request: HttpRequest, room_slug):
    """
    This function is for retriving the room and show the detail of it in the templates
    """
    room = Room.objects.get(slug=room_slug)
    context = {'room': room}
    return render(request, 'chating/chating_room_detail.html', context)