from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView
from user.forms import UserRegistrationForm, UserUpdateForm
from user.models import CustomUser


class UserLogin(LoginView):
    """Класс входа"""
    template_name = 'user/login.html'

    def get_success_url(self):
        return reverse_lazy('shop:index')


class LogoutView(View):
    """Класс выхода"""
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('shop:index'))

