from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView
from user.forms import UserRegistrationForm, UserUpdateForm
from user.models import CustomUser


class SignUp(CreateView):
    """Класс регистрации"""
    form_class = UserRegistrationForm
    success_url = 'shop:index'
    template_name = 'user/register.html'

    """Автоматический логи после регистрации"""
    def form_valid(self, form):
        """сохраняем юзера"""
        form.save()
        """аутенфицируем юзера"""
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password1'],)
        login(self.request, user)
        return HttpResponseRedirect(reverse('user:personal_area'))


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


class PersonalArea(LoginRequiredMixin, ListView):
    """Класс личного кабинета"""
    login_url = 'login'
    model = CustomUser
    template_name = 'user/personal_area.html'


class UpdateUser(LoginRequiredMixin, UpdateView):
    """Класс обновления юзера"""
    login_url = 'login'
    model = CustomUser
    template_name = 'user/update_user.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('user:personal_area')

    def dispatch(self, request, *args, **kwargs):
        """проверка данных перед ответом """
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('user:login'))
        obj = self.get_object()
        if obj.id != self.request.user.id:
            return render(request, '404.html')
        return super(UpdateUser, self).dispatch(request, *args, **kwargs)
