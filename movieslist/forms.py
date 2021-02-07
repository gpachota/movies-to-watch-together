from django import forms

from .models import Movie, MovieList
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('title',)


class MovieListForm(forms.ModelForm):

    class Meta:
        model = MovieList
        fields = ('list_name',)


class RegisterForm(forms.Form):
    pass

