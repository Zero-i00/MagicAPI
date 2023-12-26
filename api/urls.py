from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Magic API",
      default_version='v1',
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="magic@gmail.com"),
      license=openapi.License(name="Magic License"),
   ),
   public=True,
   permission_classes=[permissions.IsAdminUser],
)

urlpatterns = [
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls')),
]