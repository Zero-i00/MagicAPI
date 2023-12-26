from django.contrib import admin

from order.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'seller', 'product', 'datetime', )
    list_filter = ('datetime', )


admin.site.register(Order, OrderAdmin)
