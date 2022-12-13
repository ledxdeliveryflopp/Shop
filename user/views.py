from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView
from user.forms import UserRegistrationForm


class SignUp(CreateView):
    form_class = UserRegistrationForm
    success_url = 'shop:index'
    template_name = 'user/register.html'

    """Автоматический логи после регистрации"""
    def form_valid(self, form):
        """сохраняем юзера"""
        form.save()
        """сохраняем юзера"""
        username = self.request.POST['username']
        password = self.request.POST['password1']
        """аутенфицируем юзера"""
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password1'],)
        login(self.request, user)
        return HttpResponseRedirect(reverse('shop:index'))


class UserLogin(LoginView):
    template_name = 'user/login.html'

    def get_success_url(self):
        return reverse_lazy('shop:index')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('shop:index'))
