from django.shortcuts import render
from .models import Room, Message
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, DeleteView
from .forms import RoomForm
from django.urls import reverse_lazy
from django.db.models import Q


@login_required
def rooms(request: HttpRequest):
    """
    this function is for handling the rooms view and showing the all rooms to the user
    """
    # here is a query that i wrote , here current user just see the room has created and see the rooms
    # that users that he/she follows that they created
    rooms = Room.objects.filter(Q(owner=request.user) | Q(owner__profile__in=request.user.profile.follows.all()))
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


class CreateRoomChating(LoginRequiredMixin, FormView):
    """
    This class is for creating the room for chating and all the persons that
    follows the user who created the room can see him/her room
    """
    form_class = RoomForm
    template_name = 'room/create_room_page.html'

    def get_success_url(self):
        return reverse_lazy('rooms')

    def form_valid(self, form):
        room = form.save(commit=False)
        room.owner = self.request.user
        room.save()
        return super().form_valid(form)


class DeleteRoomView(LoginRequiredMixin, DeleteView):
    """
    This class is for deleting the room object that user want
    """
    model = Room
    success_url = reverse_lazy('rooms')
    template_name = 'room/room_confirm_delete.html'

    def get_queryset(self):
        """
        Overrides the get_queryset method to ensure that the user can only
        delete rooms they have created.
        """
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


