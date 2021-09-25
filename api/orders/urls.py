from django.urls import path
from .import views

urlpatterns = [
    path('', views.OrderList.as_view(), name='order-list'),
    path('<uuid:pk>/', views.OrderDetail.as_view(), name='order-detail'),
]
