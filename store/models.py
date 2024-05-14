from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """Сущность категории"""
    title_category = models.CharField(max_length=100, verbose_name='Название категории')
    description_category = models.TextField(verbose_name='Описание категории', **NULLABLE)

    def __str__(self):
        return f'{self.title_category}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    """Сущность подкатегории """
    title_subcategory = models.CharField(max_length=100, verbose_name='Название подкатегории')
    description_subcategory = models.TextField(verbose_name='Описание подкатегории', **NULLABLE)
    main_category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category',
                                      verbose_name='Основная категория')

    def __str__(self):
        return f'{self.title_subcategory}'

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    """Сущность продукта"""
    title_product = models.CharField(max_length=100, verbose_name='Название товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    price_with_discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена со скидкой')
    inventory_balance = models.PositiveSmallIntegerField(verbose_name='Товарный остаток', default=0)
    product_characteristics = models.TextField(verbose_name='Характеристики товара', **NULLABLE)

    category = models.ManyToManyField(Category, related_name='category_product', verbose_name='Категория товара')
    subcategory = models.ManyToManyField(Subcategory, related_name='subcategory_product',
                                         verbose_name='Подкатегория товара')

    def __str__(self):
        return f'{self.title_product} - ({self.price}, {self.inventory_balance})'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Cart(models.Model):
    """Сущность корзины"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')


class CartItem(models.Model):
    """Сущность элемента корзины"""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart', verbose_name='Корзина')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product', verbose_name='Товар')
    product_quantity = models.IntegerField(default=0, verbose_name='Количество товара')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
