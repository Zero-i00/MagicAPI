from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Magic Admin'
admin.site.index_title = 'Magic'
admin.site.site_title = 'Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
]
