from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class Order(models.Model):
    client = models.ForeignKey(
        verbose_name='Покупатель',
        to=User,
        on_delete=models.CASCADE,
        related_name='client_to_order'
    )

    seller = models.ForeignKey(
        verbose_name='Продавец',
        to=User,
        on_delete=models.CASCADE,
        related_name='seller_to_order'
    )

    product = models.ForeignKey(
        verbose_name='Товар',
        to=Product,
        on_delete=models.CASCADE,
        related_name='product_to_order'
    )

    amount = models.PositiveIntegerField(verbose_name='Количесто товара')
    datetime = models.DateTimeField(verbose_name='Дата оформления', auto_now_add=True, db_index=True)

    def __str__(self):
        return f'{self.product.title} ({self.datetime.strftime("%Y-%m-%d")})'

    def __repr__(self):
        return f'{self.product.title} ({self.datetime.strftime("%Y-%m-%d")})'

    class Meta:
        db_table = 'orders'

        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
