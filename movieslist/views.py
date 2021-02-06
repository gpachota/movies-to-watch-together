from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import MovieList, Movie

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
    movies = get_list_or_404(Movie.objects.filter(movie_list=movielist.id))

    return render(request, 'movieslist/list_detail.html', {'movielist': movielist, 'movies': movies})
