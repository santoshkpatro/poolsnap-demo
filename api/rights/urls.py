from django.urls import path
from .import views


urlpatterns = [
    path('', views.LicenceList.as_view(), name='user-licenses')
]
