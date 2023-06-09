from .models import Reporter, Article ,Publisher
from rest_framework import serializers
# from .models import Reporter


# class ReporterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reporter
#         fields = "__all__"

class ReporterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields = "__all__"

        # fields = ("first_name", "last_name")
        # read_only_fields
        #write_only_fields
class PublisherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"

class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

    reporter = ReporterSerializers()
    publisher = PublisherSerializers(many=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["reporter"] = ReporterSerializers(instance.reporter).data
        data["publisher"] = PublisherSerializers(instance.publisher.all(), many=True).data
        return data
