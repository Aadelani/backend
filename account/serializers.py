from attr import field
from rest_framework.serializers import ModelSerializer
from .models import User, Profile
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "is_staff", "is_superuser"]

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ["token", "username", "email"]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
