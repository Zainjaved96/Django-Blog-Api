from .models import  Article, Publisher
from django.contrib.auth.models import User
from rest_framework import serializers


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
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    publisher = serializers.PrimaryKeyRelatedField(queryset=Publisher.objects.all(), many=True)

    class Meta:
        model = Article
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user_id = data['user']
        user = User.objects.get(id=user_id)
        data['user'] = {
            'id': user.id,
            'username': user.username,
            'email':user.email
            # Add any other fields you want to include from the User model
        }
        data['publisher'] = PublisherSerializers(instance.publisher.all(), many=True).data
        return data
