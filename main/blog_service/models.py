from django.db import models


# Create your models here.
class Reporter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100 ,default='Independent')
    email = models.EmailField()


class Article(models.Model):
    headline = models.CharField(max_length=100)
    details = models.TextField()
    reporter = models.ForeignKey(to=Reporter,  on_delete=models.CASCADE)
