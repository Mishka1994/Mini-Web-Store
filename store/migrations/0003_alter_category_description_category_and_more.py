# Generated by Django 5.0.6 on 2024-05-13 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_subcategories_main_category_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description_category',
            field=models.TextField(blank=True, null=True, verbose_name='Описание категории'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_characteristics',
            field=models.TextField(blank=True, null=True, verbose_name='Характеристики товара'),
        ),
        migrations.AlterField(
            model_name='subcategories',
            name='description_subcategory',
            field=models.TextField(blank=True, null=True, verbose_name='Описание подкатегории'),
        ),
    ]
