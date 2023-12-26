from django.urls import include, path
from rest_framework import routers

from api.category.views import CategoryViewSet

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
