from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from api.core.serializers import UserInfoSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
