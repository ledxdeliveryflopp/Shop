# Generated by Django 3.2.16 on 2022-12-13 05:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('title', models.CharField(max_length=1000, verbose_name='название')),
                ('is_active', models.BooleanField(default=True, verbose_name='Опубликован')),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('image', models.ImageField(upload_to='product/image', validators=[django.core.validators.validate_image_file_extension], verbose_name='картинка')),
                ('description', models.CharField(max_length=50, verbose_name='описание')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company', verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукция',
            },
        ),
    ]
