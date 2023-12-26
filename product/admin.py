from django.contrib import admin

from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantity', 'price', )
    list_filter = ('quantity', 'price', )


admin.site.register(Product, ProductAdmin)
