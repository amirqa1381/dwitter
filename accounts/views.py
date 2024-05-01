from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views import View
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.urls import reverse_lazy


class RegisterView(View):
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
    form_class = LoginForm
    template_name = 'accounts/login_form.html'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('dashboard')