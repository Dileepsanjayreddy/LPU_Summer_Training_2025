from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=11, primary_key=True)
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)

    def _str_(self):
        return self.title