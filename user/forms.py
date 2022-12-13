from django.contrib.auth.forms import UserCreationForm
from django import forms

from user.models import CustomUser


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'avatar')


# class UserLoginForm(forms.ModelForm):
#
#     class Meta:
#         model = CustomUser
#         fields = ('username','password',)
