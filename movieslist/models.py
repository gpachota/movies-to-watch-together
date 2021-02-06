from django.db import models
from django.contrib.auth.models import User


class MovieList(models.Model):
    title = models.CharField(max_length=200)
    contributors = models.ManyToManyField(User)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=200)
    movie_list = models.ForeignKey(MovieList, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
