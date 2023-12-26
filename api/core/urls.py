from django.urls import include, path
from rest_framework import routers

from api.core.views import UserViewSet

router = routers.SimpleRouter()

router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
