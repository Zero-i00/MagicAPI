from rest_framework import serializers

from order.models import Order
from product.models import Product


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        product = Product.objects.get(id=validated_data.get('product').id)
        product.quantity -= validated_data.get('amount')
        product.save()

        return order
