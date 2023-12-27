from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from api.core.serializers import UserInfoSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GetUserByToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(GetUserByToken, self).post(request, *args, **kwargs)

        token_data = response.data.get('token')
        token = Token.objects.get(key=token_data)

        user = User.objects.filter(id=token.user_id)
        return Response(
            data={
                "token": token.key,
                "user": UserInfoSerializer(*user).data
            },
            status=status.HTTP_200_OK
        )
