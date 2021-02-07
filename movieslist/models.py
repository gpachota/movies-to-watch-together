from django.db import models
from django.contrib.auth.models import User


class MovieList(models.Model):
    list_name = models.CharField(max_length=200)
    contributors = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.list_name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    movie_list = models.ForeignKey(MovieList, on_delete=models.CASCADE, related_name='movie_list_name')
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE, blank=False)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return self.title
