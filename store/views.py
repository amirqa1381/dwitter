from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.views import View


class UserInformationAndJobDetailsView(View):
    def get(self, request: HttpRequest):
        """
        this function is for routing and handling the get method in the class view
        """
        pass

    def post(self, request: HttpRequest):
        """
        this function is for routing and handling the post method in the class view
        """
        pass
