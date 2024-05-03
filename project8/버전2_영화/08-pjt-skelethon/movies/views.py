from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Movie, Genre

from django.http import JsonResponse


# Create your views here.
@require_safe
def index(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        
        context = {
            'movies':movies,
        }

        return render(request, 'movies/index.html', context)


def filter_genre(request):
    if request.method == 'GET':
        genre = request.GET.get('genre')
        if genre:
            movies = Movie.objects.filter(genres__name=genre)
        else:
            movies = Movie.objects.all()

        movie_data = [{'title': movie.title} for movie in movies]
        return JsonResponse({'movies': movie_data})

@require_safe
def recommended(request):
    genres = Genre.objects.all()
    movies = Movie.objects.all()

    if request.method =='GET':
        seleced_genre_id = request.GET.get('genre_id')

        if seleced_genre_id:
            selected_genre = Genre.objects.get(pk=seleced_genre_id)
            recommended_movies = movies.filter(genres=selected_genre)
        
        else:
            recommended_movies = movies
    
    context = {
        'genres':genres,
        'movies':movies,
    }
    
    return render(request,'movies/recommended.html', context)
