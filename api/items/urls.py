from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemList.as_view(), name='item-list'),
    path('<uuid:pk>/', views.ItemDetail.as_view(), name='item-detail'),
    path('<uuid:pk>/detail/', views.ItemUserDetail.as_view(), name='item-user-detail'),
    path('<uuid:pk>/upload/', views.ItemUploadView.as_view(), name='item-upload'),
    path('uploads/', views.ItemOwnerList.as_view(), name='item-owner-list')
]
