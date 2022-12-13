from django.core.validators import validate_image_file_extension
from django.db import models

from core.models import Core


class Category(models.Model):
    category = models.CharField(max_length=50, blank=False, verbose_name='Тип компании')

    class Meta:
        verbose_name = 'Тип компании'
        verbose_name_plural = 'Типы компаний'

    def __str__(self) -> str:
        return f'{self.category}'


class Company(Core):
    image = models.ImageField(upload_to='company/image', validators=[
        validate_image_file_extension], verbose_name='картинка', blank=True)
    category = models.ManyToManyField(Category, verbose_name='Категория',  null=True)

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
