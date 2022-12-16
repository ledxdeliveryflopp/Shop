from django.core.validators import validate_image_file_extension
from django.db import models
from core.models import Core
from company.models import Company


class Category(models.Model):
    title = models.CharField(max_length=50, blank=False, unique=True,  verbose_name='Категория '
                                                                                    'товара')

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'

    def __str__(self) -> str:
        return f'{self.title}'


class Product(Core):
    image = models.ImageField(upload_to='product/image', validators=[
        validate_image_file_extension], verbose_name='картинка', blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания',
                                null=True)
    category = models.ManyToManyField(Category, verbose_name='Категория')
    price = models.IntegerField(default=30, blank=False, null=False)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукция'

    def __str__(self) -> str:
        return f'{self.title}'
