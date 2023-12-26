from rest_framework import viewsets, permissions, serializers

from api.order.serializers import OrderSerializer
from order.models import Order
from product.models import Product



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        data = self.request.data
        product = Product.objects.filter(id=data.get('product')).first()
        if not product:
            raise serializers.ValidationError({'message': 'Product not found'})

        amount = int(data.get('amount'))
        if product.quantity < amount:
            raise serializers.ValidationError({f'message': f'Bad product quantity: {product.quantity} < {amount}'})

        return serializer.save()
