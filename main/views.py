from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Profile


def index_page(request):
    return render(request, "main/index.html")


def profile_list(request: HttpRequest):
    profiles = Profile.objects.exclude(user=request.user)
    context = {
        'profiles': profiles
    }
    return render(request, 'main/profile_list.html', context)


def profile_detail(request: HttpRequest, profile_id):
    """
    This function is for showing the profile detail to the user
    """
    user_profile = Profile.objects.prefetch_related('follows').get(pk=profile_id)
    current_user = request.user.profile
    if request.POST:
        data = request.POST['follow']
        if data == 'follow':
            current_user.follows.add(user_profile)
        elif data == 'unfollow':
            current_user.follows.remove(user_profile)
        current_user.save()
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'main/profile_detail.html', context)

