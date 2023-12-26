from django.urls import include, path
from rest_framework import routers

from api.order.views import OrderViewSet

router = routers.SimpleRouter()

router.register(r'order', OrderViewSet)

urlpatterns = [
    path('', include(router.urls))
]
