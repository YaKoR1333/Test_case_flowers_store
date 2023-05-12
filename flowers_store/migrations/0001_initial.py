# Generated by Django 4.2.1 on 2023-05-11 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, verbose_name='Комментарий к лоту')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Оставлен')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Покупатель')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_role', models.BooleanField(default=False, verbose_name='Роль продавца')),
                ('comment', models.ManyToManyField(blank=True, to='flowers_store.comment', verbose_name='Отзывы на продавца')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Shade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Оттенок цветка')),
            ],
            options={
                'verbose_name': 'Оттенок',
                'verbose_name_plural': 'Оттенки',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='TradeBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('order_number', models.CharField(max_length=50, verbose_name='№ Заказа')),
                ('description', models.TextField(verbose_name='Описание')),
                ('purchase_sum', models.IntegerField(verbose_name='Cумма')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trade_buyer', to='flowers_store.profile', verbose_name='Покупатель')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trade_seller', to='flowers_store.profile', verbose_name='Продавец')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flowers_store.status', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Вид цветка')),
                ('product_quantity', models.IntegerField(verbose_name='Количество товара')),
                ('price', models.IntegerField(verbose_name='Цена за единицу товара')),
                ('hide_mod', models.BooleanField(default=False, verbose_name='Скрытый лот')),
                ('comment', models.ManyToManyField(blank=True, to='flowers_store.comment', verbose_name='Отзывы на лоту')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flowers_store.profile', verbose_name='Продавец')),
                ('shade', models.ForeignKey(max_length=120, on_delete=django.db.models.deletion.PROTECT, to='flowers_store.shade', verbose_name='Оттенок')),
            ],
            options={
                'verbose_name': 'Лот',
                'verbose_name_plural': 'Лоты',
            },
        ),
    ]
