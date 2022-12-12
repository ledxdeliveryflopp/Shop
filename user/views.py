from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from shop.user import UserRegistrationForm
from shop.user.models import CustomUser


class Register(CreateView):
    """Класс регистрации юзера"""
    model = CustomUser
    form_class = UserRegistrationForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('login')


# логин
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        redirect('index.html')


# выход
def logout_view(request):
    logout(request)
    redirect('index.html')
