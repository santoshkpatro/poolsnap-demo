from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemList.as_view(), name='item-list'),
    path('<uuid:pk>/', views.ItemDetail.as_view(), name='item-detail'),
    path('owner/', views.ItemOwnerList.as_view(), name='item-owner-list')
]
