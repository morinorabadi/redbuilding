from rest_framework import serializers
from . import models


class UserLogin(serializers.Serializer):
    username = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=64)
    is_boss = serializers.BooleanField(default=True)


class UserSignUp(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
