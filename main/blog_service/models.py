from django.db import models
from django.utils import timezone


# Create your models here.
class Reporter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(default='Independent', max_length=100)


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company_name = models.TextField()
    phone_no = models.CharField(max_length=100, default='None')

#TODO install djnago-utils and user Timestamp model for created_at and updated_at
class Article(models.Model):
    headline = models.CharField(max_length=100)
    details = models.TextField()
    reporter = models.ForeignKey(to=Reporter, on_delete=models.CASCADE)
    publisher = models.ManyToManyField(to=Publisher)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, )
