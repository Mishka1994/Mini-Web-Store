# Generated by Django 5.0.6 on 2024-05-14 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_cartitem_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='total',
        ),
    ]