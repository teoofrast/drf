from django.db import models
from django.contrib.auth.models import User


class Manufacturer(models.Model):
    '''
    Модель для представления производителя часов

    Атрибуты:
    - name (str): Название производителя
    - time_created (datetime): Дата создания
    - time_updated (datetime): Дата обновления
    '''
    name = models.CharField(max_length=255)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Watch(models.Model):
    '''
    Модель для представления часов

    Атрибуты:
    - name (str): Название часов
    - description (str): Описание часов
    - price (decimal): Цена часов
    - time_created (datetime): Дата создания
    - time_updated (datetime): Дата обновления
    - is_active (bool): Доступность товара
    '''
    name = models.CharField(max_length=255)
    description = models.TextField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, default=1, related_name='watches')
    price = models.DecimalField(max_digits=22, decimal_places=2)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name




class Basket(models.Model):
    """
    Модель для представления корзины пользователя.

    Атрибуты:
    - user (User): Пользователь, которому принадлежит корзина.
    - created_at (datetime): Дата и время создания корзины.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина пользователя {self.user}'


class BasketItem(models.Model):
    """
    Модель для представления товара в корзине.

    Атрибуты:
    - product (Watch): Товар, добавленный в корзину.
    - basket (Basket): Корзина, в которой находится товар.
    - quantity (int): Количество товара в корзине.
    """
    product = models.ForeignKey(Watch, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.product} - {self.quantity}'
