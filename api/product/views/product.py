from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from api.product.serializers import ProductSerializer
from product.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class GetPotionProducts(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(categories__title__icontains='Зелья')
        return Response(data={"products": ProductSerializer(products, many=True).data})
