from django.db import models

# Create your models here.

class Book(models.Model):
    code = models.CharField(max_length=13, unique=True)
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=250)

    def __str__(self):
        return self.name