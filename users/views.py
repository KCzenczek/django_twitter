from django.contrib.auth import logout, login
from django.shortcuts import render, redirect

# Create your views here.
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views import View

from users.forms import LoginForm
from users.models import TwitterUser


class LoginView(View):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get(self, request):
        form = self.form_class()
        return TemplateResponse(request, self.template_name, {
            'form': form,
        })

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect('/')
        else:
            return TemplateResponse(request, self.template_name, {
                'form': form,
            })
        

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class UserDetailedView(View):
    def get(self, request, pk):
        user = TwitterUser.objects.get(id=pk)
        return TemplateResponse(request, 'users/user_detail.html', {
            'user': user,
        })
