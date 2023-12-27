from django.urls import include, path
from rest_framework import routers

from api.core.views import UserViewSet
from api.core.views.user import GetUserByToken

router = routers.SimpleRouter()

router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('me/', GetUserByToken.as_view())
]
