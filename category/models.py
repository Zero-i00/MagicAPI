from django.db import models

from MagicAPI.constants import CHAR_FIELD_DEFAULT_VALUE


class Category(models.Model):
    title = models.CharField(verbose_name='Название', max_length=CHAR_FIELD_DEFAULT_VALUE)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        db_table = 'categories'

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
