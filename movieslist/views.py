from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import MovieList, Movie
from .forms import MovieForm, MovieListForm, CustomUserCreationForm
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required


def main_page(request):
    if request.user.is_authenticated:
        lists = MovieList.objects.filter(contributors=request.user)
        form = MovieListForm(request.POST or None)
        if form.is_valid():
            movie_list = form.save(commit=False)
            movie_list.save()
            movie_list.contributors.add(request.user)
            return redirect('main_page')
    else:
        lists = None
        form = MovieListForm()

    return render(request, 'movieslist/main_page.html', {'lists': lists, 'form': form})


@login_required
def list_detail(request, pk):
    movielist = get_object_or_404(MovieList, pk=pk)
    contributors = movielist.contributors
    movies = Movie.objects.filter(movie_list=movielist.id)

    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.author = request.user
            movie.movie_list = movielist
            movie.save()
            return redirect('list_detail', pk=pk)
    else:
        form = MovieForm()
    return render(request, 'movieslist/list_detail.html', {'movielist': movielist, 'movies': movies,
                                                           'contributors': contributors, 'form': form})


@login_required()
def movie_remove(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('list_detail', pk=movie.movie_list.pk)


@login_required()
def list_remove(request, pk):
    list = get_object_or_404(MovieList, pk=pk)
    list.delete()
    return redirect('main_page')


def register(request):
    if request.method == "GET":
        return render(
            request, "movieslist/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("main_page"))