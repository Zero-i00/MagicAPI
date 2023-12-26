from django.urls import include, path
from rest_framework import routers

from api.product.views import ProductViewSet

router = routers.SimpleRouter()

router.register(r'product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]
