from rest_framework import serializers
from licenses.models import License
from items.models import Item
from category.models import Category
from accounts.models import User


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'name', 'profile_url']


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


class LicenseSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)

    class Meta:
        model = License
        fields = ['id', 'item', 'valid_upto', 'created_at']
