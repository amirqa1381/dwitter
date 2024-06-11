from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, update_session_auth_hash
from .forms import (LoginForm,
                    UpdateUserInfoForm,
                    RegistrationForm,
                    ImagesetForm,
                    UserPasswordChangeForm,
                    ContactUserForm
                    )
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import FormView
from main.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Contact, AnswersForContact


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
                messages.success(request, 'The Updating the information was successfully :))')
                return redirect('general_update_info')
            context = {'form': form}
            return render(request, 'accounts/general_edit_info.html', context)
        else:
            return redirect('login')


class SetImageUserOrUpdateUserImage(FormView):
    """
    This class is for setting the image for the user if user has not image yet ,
    or update the user image if user has a image and wants to change it.
    """
    form_class = ImagesetForm
    template_name = 'accounts/image_page.html'

    def get_success_url(self):
        return reverse_lazy('general_update_info')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        user = request.user.id
        profile = Profile.objects.get(user=user)
        try:
            if profile.image is not None:
                context['profile_image'] = profile.image.url
            else:
                context['profile_image'] = '/media/profile_pics/american_flag.jpg'
        except:
            context['profile_image'] = '/media/profile_pics/american_flag.jpg'
        return context

    def form_valid(self, form):
        request = self.request
        image = form.cleaned_data.get('image' or None)
        current_user = User.objects.get(id=request.user.id)
        try:
            profile = Profile.objects.get(user=current_user)
            if image:
                profile.image = image
                profile.save()
                messages.success(request, "The image that you've selected has successfully set.")
        except:
            messages.error(request, "Something went wrong in saving the picture.")
        return HttpResponseRedirect(self.get_success_url())


class UserPasswordChangeView(LoginRequiredMixin, View):
    """
    This class is for changing the user password and for handling the requests that gonna go the the endpoint of this
    view
    """

    def get(self, request: HttpRequest):
        """
        This function is for handling the get request that is come to this view
        """
        form = UserPasswordChangeForm(request.user)
        context = {
            'form': form
        }
        return render(request, 'accounts/change_password.html', context=context)

    def post(self, request: HttpRequest):
        """
        this function is for handling the user updating the password in the post request
        """
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # after this code that we update the session, and we don't need to log in again the
            # django will log in us again
            update_session_auth_hash(request, user)
            messages.success(request, "The password has changed successfully.")
            return redirect('general_update_info')
        context = {
            'form': form
        }
        return render(request, 'accounts/change_password.html', context=context)


# Second way of changing the password
# class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
#     form_class = UserPasswordChangeForm
#     template_name = "accounts/change_password.html"
#
#     def get_success_url(self):
#         return reverse_lazy("general_update_info")
#
#     def form_valid(self, form):
#         user = form.save()
#         update_session_auth_hash(self.request, user)
#         return super().form_valid(form)


class ContactUserView(LoginRequiredMixin, View):
    """
    this view is for handling the user messages and contact with us
    """

    def get(self, request: HttpRequest):
        """
        this function is for handling the get method of the view and when user send
        get request to it we handel it with this function
        """
        form = ContactUserForm()
        contact_messages = Contact.objects.filter(user=request.user)
        answers = AnswersForContact.objects.filter(contact=contact_messages)
        context = {
            'form': form,
            'contact_messages': contact_messages,
            'answers': answers
        }
        return render(request, 'accounts/contact-page.html', context)

    def post(self, request: HttpRequest):
        """
        this function is for a time that user send a post request and submit a form and we should
        handel it with this function
        """
        form = ContactUserForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, 'The message sent successfully.')
            return redirect('contact')
        else:
            messages.error(request, 'Something went wrong')
        context = {
            'form': form
        }
        return render(request, 'accounts/contact-page.html', context)
