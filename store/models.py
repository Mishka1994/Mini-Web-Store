from django.db import models


class Category(models.Model):
    title_category = models.CharField(max_length=100, verbose_name='Название категории')
    description_category = models.TextField(verbose_name='Описание категории')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategories(models.Model):
    title_subcategory = models.CharField(max_length=100, verbose_name='Название подкатегории')
    description_subcategory = models.TextField(verbose_name='Описание подкатегории')
    main_category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Основная категория')

    def __str__(self):
        return f'{self.title_subcategory}'

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'



