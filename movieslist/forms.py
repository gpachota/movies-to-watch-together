from django import forms

from .models import Movie, MovieList


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('title',)


class MovieListForm(forms.ModelForm):

    class Meta:
        model = MovieList
        fields = ('title', 'contributors',)
