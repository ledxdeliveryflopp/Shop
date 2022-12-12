from django.db import models


class Core(models.Model):
    title = models.CharField(max_length=1000, verbose_name="название")
    is_active = models.BooleanField(default=True, verbose_name='Опубликован')
    id = models.AutoField(primary_key=True, unique=True, verbose_name='id')

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        abstract = True
