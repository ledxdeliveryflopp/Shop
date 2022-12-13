from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from user.forms import UserRegistrationForm
from user.models import CustomUser

class Register(FormView):
    template_name = 'user/register.html'
    form_class = UserRegistrationForm
    success_url = 'index'

    def form_valid(self, form):
        #save the new user first
        form.save()
        #get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        #authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url)



def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        redirect('index.html')


def logout_view(request):
    logout(request)
    redirect('index.html')
