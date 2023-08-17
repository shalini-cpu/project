from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)
    roll = models.IntegerField()
    section = models.CharField(max_length=5)
    age = models.IntegerField(null=True, blank=True)

