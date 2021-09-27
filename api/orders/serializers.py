from rest_framework import serializers
from orders.models import Order
from items.models import Item
from orders.models import Order
from category.models import Category
from accounts.models import User


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'profile_url']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ItemSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'owner', 'category', 'resource_url']


class OrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'item', 'type', 'price', 'amount', 'discount', 'status', 'transaction_id', 'created_at']
