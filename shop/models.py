from django.core.validators import validate_image_file_extension
from django.db import models

from core.models import Core
# blank=False, null=False,
from company.models import Company


class Product(Core):
    image = models.ImageField(upload_to='product/image', validators=[
        validate_image_file_extension], verbose_name='картинка', blank=False)
    description = models.CharField(max_length=50, verbose_name='описание')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания', null=True)
    # company = models.ManyToManyField()

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукция'

    def __str__(self) -> str:
        return f'{self.title}'
