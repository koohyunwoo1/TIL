from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Actor, Movie, Review
from django.shortcuts import get_object_or_404 ,get_list_or_404
from .serializers import ActorListSeiralizers, ActorSeiralizers, MovieListSeiralizers, MovieSerializers, ReviewListSerializers
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def actor_list(request):
    # actors = Actor.objects.all()
    actors = get_list_or_404(Actor)
    serializer = ActorListSeiralizers(actors, many=True)
    return Response(serializer.data)

        
@api_view(['GET'])
def actor_detail(request, actors_pk):
    # actor = Actor.objects.get(pk=actors_pk)
    actor = get_object_or_404(Actor, pk=actors_pk)
    serializer = ActorSeiralizers(actor)
    return Response(serializer.data)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSeiralizers(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieSerializers(movie)
    return Response(serializer.data)


@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializers(reviews, many=True)  # many=True를 사용하여 여러 객체를 직렬화합니다.
    return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
def review_detail(request):
    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    else:
        pass

@api_view(['POST'])
def create_review(request):
    pass