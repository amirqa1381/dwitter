from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views import View
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .forms import LoginForm, UpdateUserInfoForm
from django.urls import reverse_lazy
from django.contrib import messages

class RegisterView(View):
    """
    This class is for registering the user into the site application.
    """
    def get(self, request: HttpRequest):
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'accounts/register_page.html', context)

    def post(self, request: HttpRequest):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User.objects.create_user(user_name, email, password)
            if first_name or last_name:
                user.first_name = first_name
                user.last_name = last_name
            user.save()
            messages.success(request, "Account created")
            return redirect('dashboard')
        context = {
            'form': form
        }
        return render(request, 'accounts/register_page.html', context)


class Login(LoginView):
    """
    This class is for logging the user into site
    """
    form_class = LoginForm
    template_name = 'accounts/login_form.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')


def logout_view(request):
    """
    This function is for logging out the user from the site
    """
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('dashboard')



class UpdateUserInfo(View):
    """
    This class is for updating the user information.
    """
    def get(self, request: HttpRequest):
        """
        This function is for get method and when user requested to the site
        """
        current_user = User.objects.get(id=request.user.id)
        form = UpdateUserInfoForm(instance=current_user)
        context = {'form': form}
        return render(request, 'accounts/general_edit_info.html', context)

    def post(self, request: HttpRequest):
        """
        This function is for the post method and when user sending a things to the site server
        """
        if request.user.is_authenticated:
            current_user = User.objects.get(id=request.user.id)
            form = UpdateUserInfoForm(request.POST, instance=current_user)
            if form.is_valid():
                form.save()
                messages.success(request,'The Updating the information was successfully :))')
                return redirect('general_update_info')
            context = {'form': form}
            return render(request, 'accounts/general_edit_info.html', context)
        else:
            return redirect('login')
