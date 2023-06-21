
from django.contrib.auth.models import User
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer


class ExtendedUserCreateSerializer(UserCreateSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("password", "username", "email", "first_name", "last_name")


