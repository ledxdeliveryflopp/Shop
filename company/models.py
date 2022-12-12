from django.core.validators import validate_image_file_extension
from django.db import models

from shop.core.models import Core


class Company(Core):
    image = models.ImageField(upload_to='company/image', validators=[
        validate_image_file_extension], verbose_name='картинка', blank=True)
    description = models.CharField(max_length=50)
    # company = models.ManyToManyField()

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
