from rest_framework import serializers
from .models import Post, Category, Comment


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class PostListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('pk', 'title', 'category')


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class CommentSerialzer(serializers.ModelSerializer):

        class Meta:
            model = Comment
            fields = '__all__'

    comment_set = CommentSerialzer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = '__all__'
        
class CommentSerialzer(serializers.ModelSerializer):
    post = PostListSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'