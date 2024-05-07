from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=100)
    department = models.CharField(default='CSE', max_length=100)
    
    def __str__(self):
        return f"{self.roll}-{self.name}"