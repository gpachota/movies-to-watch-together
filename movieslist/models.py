from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class MovieList(models.Model):
    title = models.CharField(max_length=200)
    contributors = models.ManyToManyField(User)
    movies = models.ManyToManyField(Movie, blank=True)

    def __str__(self):
        return self.title

