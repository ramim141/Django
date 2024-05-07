from django.db import models

# Create your models here.
class StudentModel(models.Model):
    roll = models.IntegerField( primary_key=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)