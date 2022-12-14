from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import Core


class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True, unique=True, verbose_name='id')
    username = models.CharField(max_length=30, unique=True, null=False, verbose_name='Логин',
                                error_messages={'unique': "Такой пользователь уже существует!"})
    avatar = models.ImageField(upload_to='user/avatars/', verbose_name='Аватарка', null=True,
                               blank=True)
    description = models.CharField(max_length=50, null=True, blank=True, verbose_name='описание')

    def __str__(self):
        return self.username
