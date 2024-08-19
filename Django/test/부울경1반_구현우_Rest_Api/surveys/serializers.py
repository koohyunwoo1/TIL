from rest_framework import serializers
from .models import Topic, Question, Choice, Answer


###### Topic Serailzier#######

# 모든 topic 리스트 가져오기
# 문제 1. title 필드만 가져와서 볼 수 있도록 수정하기
class TopicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('title',)
        read_only_fields = []


# 특정 topic 디테일 정보 가져오기
class TopicDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
        read_only_fields = []


# Topic 생성 혹은 수정 할 때 사용
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
        read_only_fields = []


##### Question Serializer

# 모든 질문 리스트의 text 필드를 가져와야 함
class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', ]
        read_only_fields = []


# Question 생성, 수정에서 사용
# 문제 2. topic 필드가 필수 입력이 되지 않도록 수정
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('text',)
        read_only_fields = []


# 등록된 choice 의 text 정보를 볼 수 있어야 함
# 등록된 모든 answer의 개수를 볼 수 있어야 함
class QuestionDetailSerializer(serializers.ModelSerializer):
    class QuestionChoiceSerializer(serializers.ModelSerializer):
        class Meta:
            model = Choice
            fields = ['text']
    # 문제 3. QuestionChoiceSerializer 를 이용하여 choice_set 필드 수정하기
    choice_set = QuestionChoiceSerializer(read_only=True, many=True)
    # 문제 4. total_answer 필드 추가하기
    # total_answer는 해당 문제에 달린 모든 answer의 개수를 리턴하는 필드이다.
    total_answer = Answer.objects.get
    
    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = []


##### Choice Serailzer

# 등록된 선택지의 text를 보여주기 위함
class ChoiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text',]
        read_only_fields = []


# 선택지 생성, 수정시 사용
class ChoiceSerializer(serializers.ModelSerializer):
    class QuestionChoiceSerializer(serializers.ModelSerializer):
        class Meta:
            model = Question
            fields = ['id', 'text',]
    
    question = QuestionChoiceSerializer(read_only=True)
    class Meta:
        model = Choice
        fields = '__all__'
        read_only_fields = []


##### Answer Serializer

# 선택지에 등록된 모든 답변을 보여줘야 함
class AnswerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['comment', ]
        read_only_fields = []


# 답변 등록을 위해 사용
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = ['question', 'choice',]


# 답변 수정을 위해 사용
class AnswerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = []