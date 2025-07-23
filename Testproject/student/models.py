from django.db import models

class Student(models.Model):
    roll_number = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    address = models.TextField()
    phone = models.PositiveIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


