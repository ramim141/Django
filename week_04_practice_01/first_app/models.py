from django.db import models


class PracticeModel(models.Model):
    roll = models.IntegerField()
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    # bigAutoField = models.BigAutoField()
    # bigAutoInt = models.BigIntegerField()
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
