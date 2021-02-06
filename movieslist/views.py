from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import MovieList, Movie
from .forms import MovieForm
from django.utils import timezone

from django.contrib.auth.decorators import login_required


def main_page(request):
    if request.user.is_authenticated:
        lists = MovieList.objects.filter(contributors=request.user)
    else:
        lists = None
    return render(request, 'movieslist/main_page.html', {'lists': lists})


@login_required
def list_detail(request, pk):
    movielist = get_object_or_404(MovieList, pk=pk)
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
    return render(request, 'movieslist/list_detail.html', {'movielist': movielist, 'movies': movies, 'form': form})


@login_required()
def movie_remove(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('list_detail', pk=movie.movie_list.pk)
