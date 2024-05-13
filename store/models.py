from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название категории')
    description_category = models.TextField(verbose_name='Описание категории')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


