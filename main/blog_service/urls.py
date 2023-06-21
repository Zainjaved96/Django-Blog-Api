"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import   ArticleView, ArticleViewDetails, PublisherView, PublisherViewDetails, ExtendedUserCreateView


urlpatterns = [
    # path("reporter/", ReporterView.as_view()),
    # path("reporter/<int:pk>/", ReporterView.as_view())
    #
    # path("reporter/", ReporterView.as_view()),
    # path("reporter/<int:pk>", ReporterViewDetails.as_view()),

    path("article/", ArticleView.as_view()),
    path("article/<int:pk>", ArticleViewDetails.as_view()),

    path("publisher/", PublisherView.as_view()),
    path("publisher/<int:pk>", PublisherViewDetails.as_view()),

    path('users/', ExtendedUserCreateView.as_view(), name='user-create'),

]
