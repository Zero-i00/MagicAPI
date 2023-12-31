from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from MagicAPI import settings

admin.site.site_header = 'Magic Admin'
admin.site.index_title = 'Magic'
admin.site.site_title = 'Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

