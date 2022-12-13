from django.contrib.auth.forms import UserCreationForm

from user.models import CustomUser


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'avatar')
