from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import Reporter , Article, Publisher
from .serializers import ReporterSerializers , ArticleSerializers, PublisherSerializers
from rest_framework import generics, response, status


# from rest_framework import generics
# from .models import Reporter
# from .serializers import ReporterSerializer


# Create your views here.
# class ReporterView(generics.ListCreateAPIView):
#     permission_classes = []
#     queryset = Reporter.objects.all()
#     serializer_class = ReporterSerializers
# class ReporterViewDetails(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = []
#     queryset = Reporter.objects.all()
#     serializer_class = ReporterSerializers


class ReporterView(generics.GenericAPIView):
    permission_classes = []
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializers

    def get(self, *args, **kwargs):
        data = self.queryset.all()
        paginated = self.paginate_queryset(data)
        serialized = self.get_serializer(paginated, many=True)
        return self.get_paginated_response(serialized.data)

    def post(self, request, *args, **kwargs):
        serialized = self.get_serializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return response.Response(serialized.data, status=status.HTTP_201_CREATED)
        return response.Response(serialized.eroors, status=status.HTTP_400_BAD_REQUEST)


class ReporterViewDetails(generics.GenericAPIView):
    permission_classes = []
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializers

    def get(self, request, *args, **kwargs):
        try:
            if kwargs.get("pk"):
                data = self.queryset.get(pk=kwargs.get('pk'))
                serialized = self.get_serializer(data)
                return response.Response(serialized.data)
        except ObjectDoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            data = self.queryset.get(pk=kwargs.get('pk'))
            serialized = self.get_serializer(data, data=request.data)
            if serialized.is_valid():
                serialized.save()
                return response.Response(serialized.data)
            return response.Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            data = self.queryset.get(pk=kwargs.get('pk'))
            data.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



class ArticleView(generics.GenericAPIView):
    permission_classes = []
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers

    def get(self, *args, **kwargs):
        data = self.queryset.all()
        paginated = self.paginate_queryset(data)
        serialized = self.get_serializer(paginated, many=True)
        return self.get_paginated_response(serialized.data)

    def post(self, request, *args, **kwargs):
        serialized = self.get_serializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return response.Response(serialized.data, status=status.HTTP_201_CREATED)
        return response.Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleViewDetails(generics.GenericAPIView):
    permission_classes = []
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers

    def get(self, request, *args, **kwargs):
        try:
            if kwargs.get("pk"):
                data = self.queryset.get(pk=kwargs.get('pk'))
                serialized = self.get_serializer(data)
                return response.Response(serialized.data)
        except ObjectDoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            data = self.queryset.get(pk=kwargs.get('pk'))
            serialized = self.get_serializer(data, data=request.data)
            if serialized.is_valid():
                serialized.save()
                return response.Response(serialized.data)
            return response.Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            data = self.queryset.get(pk=kwargs.get('pk'))
            data.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class PublisherView(generics.GenericAPIView):
    permission_classes = []
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializers

    def get(self, *args, **kwargs):
        data = self.queryset.all()
        paginated = self.paginate_queryset(data)
        serialized = self.get_serializer(paginated, many=True)
        return self.get_paginated_response(serialized.data)

    def post(self, request, *args, **kwargs):
        serialized = self.get_serializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return response.Response(serialized.data, status=status.HTTP_201_CREATED)
        return response.Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class PublisherViewDetails(generics.GenericAPIView):
    permission_classes = []
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializers

    def get(self, request, *args, **kwargs):
        try:
            if kwargs.get("pk"):
                data = self.queryset.get(pk=kwargs.get('pk'))
                serialized = self.get_serializer(data)
                return response.Response(serialized.data)
        except ObjectDoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            data = self.queryset.get(pk=kwargs.get('pk'))
            serialized = self.get_serializer(data, data=request.data)
            if serialized.is_valid():
                serialized.save()
                return response.Response(serialized.data)
            return response.Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            data = self.queryset.get(pk=kwargs.get('pk'))
            data.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)