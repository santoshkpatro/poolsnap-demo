from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('api.auth.urls')),
    path('api/items/', include('api.items.urls')),
    path('api/licenses/', include('api.rights.urls')),
    path('api/orders/', include('api.orders.urls')),
    path('api/categories/', include('api.categories.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
