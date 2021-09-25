from django.urls import path
from .import views


urlpatterns = [
    path('user/', views.UserRightList.as_view(), name='user-rights')
]
