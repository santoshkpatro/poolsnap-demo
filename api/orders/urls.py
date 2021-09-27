from django.urls import path
from .import views

urlpatterns = [
    path('', views.OrderList.as_view(), name='order-list'),
    path('<uuid:pk>/', views.OrderDetail.as_view(), name='order-detail'),
    path('create/<uuid:item_id>/', views.order_create, name='create-order'),
    path('process/<uuid:pk>/', views.order_process, name='order-proccess'),
]
