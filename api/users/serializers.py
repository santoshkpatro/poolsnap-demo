from rest_framework import serializers
from accounts.models import User
from items.models import Item


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'name', 'profile_url']
