from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=11, primary_key=True)
    title = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=100, null=False)
    published_year = models.IntegerField(null=False)

