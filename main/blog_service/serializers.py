from .models import Article, Publisher
from rest_framework import serializers
from user.serializers import ExtendedUserCreateSerializer


class PublisherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "headline", "details", "publisher", "user"]
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data["user"] = self.context['request'].user
        return super().create(validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['publisher'] = PublisherSerializers(instance.publisher.all(), many=True).data
        representation['user'] = ExtendedUserCreateSerializer(instance.user).data
        return representation
