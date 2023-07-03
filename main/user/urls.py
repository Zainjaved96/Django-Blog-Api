from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import custom_password_reset_redirect
urlpatterns = [

    path('', include('djoser.urls')),
    path('password-confirm/<str:uid>/<str:token>/', custom_password_reset_redirect,
         name='custom_password_reset_redirect'),
]
