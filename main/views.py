from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Profile



def index_page(request):
    return render(request, "main/index.html")


def profile_list(request: HttpRequest):
    profiles = Profile.objects.exclude(user=request.user)
    context = {
        'profiles' : profiles
    }
    return render(request, 'main/profile_list.html', context)