from django.db import models
from django.contrib.auth.models import User


class Shade(models.Model):
    title = models.CharField(max_length=150, verbose_name='Оттенок цветка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Оттенок'
        verbose_name_plural = 'Оттенки'
        ordering = ['title']


class Status(models.Model):
    title = models.CharField(max_length=150, verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Comment(models.Model):
    text = models.TextField(blank=True, verbose_name='Комментарий к лоту')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Покупатель')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Оставлен')

    def __str__(self):
        return f'Отззыв оставил покупатель {self.user.username}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    sales_role = models.BooleanField(default=False, verbose_name='Продавец')
    comment = models.ManyToManyField(Comment, blank=True, verbose_name='Отзывы на продавца')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Lot(models.Model):
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Продавец')
    title = models.CharField(max_length=150, verbose_name='Вид цветка')
    shade = models.ForeignKey(Shade, on_delete=models.PROTECT, null=False, max_length=120, verbose_name='Оттенок')
    product_quantity = models.IntegerField(verbose_name='Количество товара')
    price = models.IntegerField(verbose_name='Цена за единицу товара')
    hide_mod = models.BooleanField(default=False, verbose_name='Скрытый лот')
    comment = models.ManyToManyField(Comment, blank=True, verbose_name='Отзывы на лот')

    def __str__(self):
        return f'лот:{self.title} оттенка:{self.shade} продавец:{self.seller.user.username}'

    class Meta:
        verbose_name = 'Лот'
        verbose_name_plural = "Лоты"


class TradeBook(models.Model):
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Продавец', related_name='trade_seller')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    order_number = models.CharField(max_length=50, verbose_name='№ Заказа')
    description = models.TextField(blank=False, verbose_name='Описание')
    buyer = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Покупатель', related_name='trade_buyer')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус')
    purchase_sum = models.IntegerField(verbose_name='Cумма')

    def __str__(self):
        return f'Закказ номер:{self.order_number} продавец:{self.seller.user.username} покупатель:{self.buyer}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
