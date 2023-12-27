from django.urls import include, path
from rest_framework import routers

from api.product.views import ProductViewSet
from api.product.views.product import GetPotionProducts

router = routers.SimpleRouter()

router.register(r'product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('potions', GetPotionProducts.as_view())
]
