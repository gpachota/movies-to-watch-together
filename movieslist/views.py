from django.shortcuts import render


def main_page(request):
    return render(request, 'movieslist/main_page.html', )