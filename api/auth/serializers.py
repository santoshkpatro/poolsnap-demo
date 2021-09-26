from rest_framework import serializers
from accounts.models import User
from rest_framework_simplejwt.tokens import AccessToken


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'phone', 'profile_url', 'token']

    def get_token(self, obj):
        return str(AccessToken.for_user(obj))
