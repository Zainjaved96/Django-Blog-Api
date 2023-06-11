from django.db import models


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


class Article(models.Model):
    headline = models.CharField(max_length=100)
    details = models.TextField()
    reporter = models.ForeignKey(to=Reporter, on_delete=models.CASCADE)
    publisher = models.ManyToManyField(to=Publisher)
