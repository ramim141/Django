from django.db import models
from musicians.models import Musician


class Album(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 10)])

    def __str__(self):
        return self.album_name