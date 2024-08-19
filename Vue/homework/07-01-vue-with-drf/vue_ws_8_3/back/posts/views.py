from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .serializers import PostListSerializer
from .models import Post

# Create your views here.

@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serialzers = PostListSerializer(posts, many=True)
    return Response(serialzers.data)