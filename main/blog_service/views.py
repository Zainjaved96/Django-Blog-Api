from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import Article, Publisher
from .serializers import ArticleSerializers, PublisherSerializers
from rest_framework import generics, response, status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# class ReporterView(generics.GenericAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Reporter.objects.all()
#     serializer_class = ReporterSerializers
#
#     # Updating Swagger
#     @swagger_auto_schema(
#         manual_parameters=[
#             openapi.Parameter('search_key', openapi.IN_QUERY,
#                               default=None, required=False,
#                               type=openapi.TYPE_STRING,
#                               description="send search key"
#                               ),
#
#         ]
#     )
#     def get(self, request, *args, **kwargs):
#
#         search_key = request.GET.get("search_key")
#
#         if search_key:
#             data = self.queryset.filter(Q(first_name__startswith=search_key) | Q(last_name__startswith=search_key))
#         else:
#             data = self.queryset.all()
#
#         paginated = self.paginate_queryset(data)
#         serialized = self.get_serializer(paginated, many=True)
#         return self.get_paginated_response(serialized.data)
#
#     def post(self, request, *args, **kwargs):
#         serialized = self.get_serializer(data=request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return response.Response(serialized.data, status=status.HTTP_201_CREATED)
#         return response.Response(serialized.eroors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ReporterViewDetails(generics.GenericAPIView):
#     permission_classes = []
#     queryset = Reporter.objects.all()
#     serializer_class = ReporterSerializers
#
#     def get(self, request, *args, **kwargs):
#         try:
#             if kwargs.get("pk"):
#                 data = self.queryset.get(pk=kwargs.get('pk'))
#                 serialized = self.get_serializer(data)
#                 return response.Response(serialized.data)
#         except ObjectDoesNotExist:
#             return response.Response(status=status.HTTP_404_NOT_FOUND)
#
#     def put(self, request, *args, **kwargs):
#         if kwargs.get("pk"):
#             data = self.queryset.get(pk=kwargs.get('pk'))
#             serialized = self.get_serializer(data, data=request.data)
#             if serialized.is_valid():
#                 serialized.save()
#                 return response.Response(serialized.data)
#             return response.Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
#         return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
#     def delete(self, request, *args, **kwargs):
#         if kwargs.get("pk"):
#             data = self.queryset.get(pk=kwargs.get('pk'))
#             data.delete()
#             return response.Response(status=status.HTTP_204_NO_CONTENT)
#         return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ArticleView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('search_key', openapi.IN_QUERY,
                              default=None, required=False,
                              type=openapi.TYPE_STRING,
                              description="send search key"
                              ),

        ]
    )
    def get(self, request, *args, **kwargs):
        search_key = request.GET.get("search_key")

        queryset = self.queryset

        if search_key:
            data = queryset.filter(
                Q(headline__icontains=search_key) |
                Q(reporter__first_name__icontains=search_key) |
                Q(reporter__last_name__icontains=search_key)
            )
        else:
            data = queryset.all()
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

    # Updating Swagger
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('search_key', openapi.IN_QUERY,
                              default=None, required=False,
                              type=openapi.TYPE_STRING,
                              description="send search key"
                              ),

        ]
    )
    def get(self, request, *args, **kwargs):
        search_key = request.GET.get("search_key")

        if search_key:
            data = self.queryset.filter(Q(name__startswith=search_key) | Q(company_name__startswith=search_key))
        else:
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

# Extend the user create view
# class ExtendedUserCreateView(generics.CreateAPIView):
#     serializer_class = ExtendedUserCreateSerializer
#
#     def perform_create(self, serializer):
#         user = serializer.save()
#         user.is_active = True  # Set the user account as active
#         user.save()
