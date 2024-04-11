from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        # 여기서는 articles가 QuerySet이기 때문에 입력해줘야 된다.
        # Serialize 대상이 QuerySet인 경우 입력
        # 다중 데이터이기 때문에 many를 꼭 True로 해줘야 된다.
        return Response(serializer.data)
        # Serialized data 객체에서 실제 데이터를 추출
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk = article_pk)
    if request.method == 'GET':
        # 단일데이터
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial = True)
        # partial 인자 값이 False일 경우 게시글 title만을 수정하려고 해도 
        # 반드시 content 값도 요쳥 시 함께 전송해야 함

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



