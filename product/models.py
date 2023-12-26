from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from django.db import models
from MagicAPI.constants import CHAR_FIELD_DEFAULT_VALUE, TEXT_FIELD_DEFAULT_VALUE
from category.models import Category


class Product(models.Model):
    title = models.CharField(verbose_name='Название', max_length=CHAR_FIELD_DEFAULT_VALUE)
    required_magic_power = models.PositiveSmallIntegerField(
        verbose_name='Необходимый магический уровень',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(99)
        ],
        db_index=True
    )

    quantity = models.PositiveIntegerField(verbose_name='В наличии', db_index=True)
    categories = models.ManyToManyField(
        verbose_name='Категории',
        to=Category,
        blank=True,
        related_name='categories_to_product'
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='products',
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])]
    )

    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    description = models.TextField(
        verbose_name='Описание',
        max_length=TEXT_FIELD_DEFAULT_VALUE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.title} ({self.quantity})'

    def __repr__(self):
        return f'{self.title} ({self.quantity})'

    class Meta:
        db_table = 'products'

        verbose_name = 'Товар',
        verbose_name_plural = 'Товары'
