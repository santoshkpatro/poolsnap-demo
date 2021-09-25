from rest_framework import serializers
from rights.models import Right
from items.models import Item
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


class RightSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)

    class Meta:
        model = Right
        fields = ['id', 'item', 'valid_upto', 'created_at']
