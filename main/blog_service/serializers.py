from .models import Article, Publisher
from django.contrib.auth.models import User
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer


class ExtendedUserCreateSerializer(UserCreateSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta(UserCreateSerializer.Meta):
        fields = UserCreateSerializer.Meta.fields + ('first_name', 'last_name')


# from .models import Reporter


# class ReporterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reporter
#         fields = "__all__"


class PublisherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"


class ArticleSerializers(serializers.ModelSerializer):
    publisher = serializers.PrimaryKeyRelatedField(queryset=Publisher.objects.all(), many=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = ["headline", "details", "publisher", "user"]
        read_only_fields = ['user']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user_id = data['user']
        data['user'] = user_id
        data['publisher'] = PublisherSerializers(instance.publisher.all(), many=True).data
        return data

