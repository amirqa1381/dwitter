from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Profile, Dweet
from .forms import DweetForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


# def index_page(request):
#     """
#     This function is for rendering the main page of the application.
#     """
#     return render(request, "main/index.html")


def profile_list(request: HttpRequest):
    """
    This function is for displaying the all profiles.
    """
    profiles = Profile.objects.exclude(user=request.user)
    context = {
        'profiles': profiles
    }
    return render(request, 'main/profile_list.html', context)


def profile_detail(request: HttpRequest, profile_id):
    """
    This function is for showing the profile detail to the user
    """
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()
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


@login_required
def dashboard(request: HttpRequest):
    """
    This function is for displaying the dweets of the user's profile that i followed and a form
    for submitting my dweets
    """
    if request.method == "GET":
        form = DweetForm()
        followed_dweets = Dweet.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by(
            '-created_at')
        context = {
            'form': form,
            'followed_dweets': followed_dweets
        }
        return render(request, 'main/dashboard.html', context)

    if request.method == "POST":
        form = DweetForm(request.POST, request.FILES)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            messages.success(request, 'Your dweet has been submitted!')
            return redirect('dashboard')
        messages.error(request, "Invalid dweet")
        context = {
            'form': form
        }
        return render(request, 'main/dashboard.html', context)


class AboutView(TemplateView):
    """
    this class is for showing the template to the user and tell to user all the
    functionality and features of this website
    """
    template_name = 'main/about.html'