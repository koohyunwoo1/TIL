from rest_framework import serializers
from .models import Actor, Review, Movie


#  배우 정보 제공


class ActorListSeiralizers(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'


class ActorSeiralizers(serializers.ModelSerializer):
    class ActorMovieSeiralizers(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('title',)
        
    Movies = ActorMovieSeiralizers(read_only = True, many =True)


    class Meta:
        model = Actor
        fields = '__all__'



# 영화 목록 제공

class MovieListSeiralizers(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)


class MovieSerializers(serializers.ModelSerializer):
    class MovieReviewSerializers(serializers.ModelSerializer):

        class Meta:
            model = Review
            fields = ('title','content',)

    review_set = MovieReviewSerializers(read_only = True, many = True)

    class Meta:
        model = Movie
        fields = '__all__'


# 전체 리뷰 목록 제공

class ReviewListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content',)

# 단일 리뷰 조회 & 수정 & 삭제


