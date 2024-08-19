from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class ArticleSerializer(serializers.ModelSerializer):
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id','content',)
            # read_only_fields = ('article',)

    comment_set = CommentDetailSerializer(read_only = True, many = True)
    # 이름이 정해져 있음
    comment_cnt = serializers.IntegerField(source ='comment_set.cnt', read_only = True)

    # 이름이 정해져 있지 않다.
    # 새로운 필드

    class Meta:
        model = Article
        fields = '__all__'


# 댓글을 제공해주는 Serializer 클래스

class CommentSerializer(serializers.ModelSerializer):
    # 어떤 게시글이 달린 댓글인지 알아보기
    class ArticletitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    # 출력결과를 좀 더 세부적으로 알려주기
    article = ArticletitleSerializer(read_only = True)
    # -----

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)
        # 유효성 검사에서 제외시키고, 데이터 조회 시에는 출력 