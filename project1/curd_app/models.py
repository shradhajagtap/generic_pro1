from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    div = models.CharField(max_length=10)

    def __str__(self):
        return self.name
