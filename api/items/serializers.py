from rest_framework import serializers
from accounts.models import User
from items.models import Item
from category.models import Category


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
    category_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Item
        fields = ['id', 'owner', 'category_id', 'category', 'resource_url', 'description', 'monthly_price',
                  'monthly_discount', 'yearly_price', 'yearly_discount', 'created_at']

    def create(self, validated_data):
        category_id = validated_data.pop('category_id')
        try:
            category = Category.objects.get(id=category_id)
            item = super().create(validated_data)
            item.category = category
            item.save()

            return item
        except Category.DoesNotExist:
            raise serializers.ValidationError('invalid category id')

    def update(self, instance, validated_data):
        if 'category_id' in validated_data:
            category_id = validated_data.pop('category_id')
            try:
                category = Category.objects.get(id=category_id)
                item = super().update(instance, validated_data)
                item.category = category
                item.save()

                return item
            except Category.DoesNotExist:
                raise serializers.ValidationError('invalid category id')
        return super().update(instance, validated_data)
