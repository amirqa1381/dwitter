from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.views import View
from .forms import UserJobInformationForm
from django.contrib import messages


class UserInformationAndJobDetailsView(View):
    def get(self, request: HttpRequest):
        """
        this function is for routing and handling the get method in the class view
        """
        form = UserJobInformationForm()
        context = {
            'form': form
        }
        return render(request, 'store/jobandinfo.html', context)

    def post(self, request: HttpRequest):
        """
        this function is for routing and handling the post method in the class view
        """
        form = UserJobInformationForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, "Information's of the job and detail of the location was successfully got.")
            return redirect('dashboard')
        context = {
            'form': form
        }
        return render(request, 'store/jobandinfo.html', context)
