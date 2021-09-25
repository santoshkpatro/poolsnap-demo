from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('api.auth.urls')),
    path('api/items/', include('api.items.urls')),
    path('api/rights/', include('api.rights.urls')),
]
