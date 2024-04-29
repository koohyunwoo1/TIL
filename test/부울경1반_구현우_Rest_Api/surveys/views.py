from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Topic, Question, Choice, Answer
from .serializers import (
    TopicListSerializer,
    TopicDetailSerializer,
    TopicSerializer,
    QuestionListSerializer,
    QuestionSerializer,
    QuestionDetailSerializer,
    ChoiceListSerializer,
    ChoiceSerializer,
    AnswerListSerializer,
    AnswerSerializer,
    AnswerUpdateSerializer
)


@api_view(['GET', 'POST'])
def topic_create_list(request):
    if request.method == 'POST':
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        topics = get_list_or_404(Topic)
        serializer = TopicListSerializer(topics, many=True)
        return Response(serializer.data)
    

@api_view(['GET', 'PUT', 'DELETE'])
def topic_detail_update_delete(request, topic_pk):
    topic = get_object_or_404(Topic, pk=topic_pk)

    if request.method == 'PUT':
        serializer = TopicSerializer(topic, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        topic.delete()
        return Response({'topic': f'{topic_pk} deleted'}, status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = TopicDetailSerializer(topic)
        return Response(serializer.data)
    

@api_view(['GET', 'POST'])
def question_create_list(request, topic_pk):
    topic = get_object_or_404(Topic, pk=topic_pk)
    if request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(topic=topic)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        questions = topic.question_set.all()
        serializer = QuestionListSerializer(questions, many=True)
        return Response(serializer.data)
    
# 문제 5. DELETE 동작 후 적절한 status code 응답하기
@api_view(['GET', 'PUT', 'DELETE'])
def question_detail_update_delete(request, topic_pk, question_pk):
    question = get_object_or_404(Question, pk=question_pk)

    if request.method == 'PUT':
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        question.delete()
        return Response({'question': f'{question_pk} deleted'}, status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = QuestionDetailSerializer(question)
        return Response(serializer.data)


# 문제 6. 좋아요 증가시키고 저장하기
# 응답은 좋아요 개수를 리턴 (필드 이름은 'good_question' 으로 한다.)
@api_view(['POST'])
def question_good(request, topic_pk, question_pk):
    question = Question.objects.get(pk=question_pk)
    # good_question = question.good_question
    question.good_question += 1
    question.save()
    return Response({'good_question': f'{question.good_question}' })


# 문제 7. 특정 question의 choice만 응답 데이터로 전달하기
# 문제 8. choice 생성 시 Not NULL 에러 해결하기
@api_view(['GET', 'POST'])
def choice_create_list(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)

    if request.method == 'POST':
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(question=question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        choices = Choice.objects.filter(question=question)
        serializer = ChoiceListSerializer(choices, many=True)
        return Response(serializer.data)
    
        
@api_view(['GET', 'PUT', 'DELETE'])
def choice_detail_update_delete(request, question_pk, choice_pk):
    choice = get_object_or_404(Choice, pk=choice_pk)

    if request.method == 'PUT':
        serializer = ChoiceSerializer(choice, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        choice.delete()
        return Response({'choice': f'{choice_pk} deleted'}, status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = ChoiceSerializer(choice)
        return Response(serializer.data)

# 문제 9. 답변 리스트를 GET 요청시 에러 발생 해결하기
# 문제 10. 답변 생성 기능 구현하기 (AnswerSerializer 사용)
@api_view(['GET', 'POST'])
def answer_create_list(request, choice_pk):
    choice = get_object_or_404(Choice, pk=choice_pk)

    if request.method == 'POST':
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(choice=choice)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        answers = choice.answer_set.all()
        serializer = AnswerListSerializer(answers, many=True)
        return Response(serializer.data)
    

# 문제 11. Answer의 comment 만 수정하려고 할 때, choice 필드가 필요하다고 한다.
# 단, choice 필드 또한 수정이 가능해야 하며 comment 필드 단독으로 수정도 가능해야 한다.
@api_view(['GET', 'PUT', 'DELETE'])
def answer_detail_update_delete(request, choice_pk, answer_pk):
    answer = get_object_or_404(Answer, pk=answer_pk)
    if request.method == 'PUT':
        serializer = AnswerUpdateSerializer(answer, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        answer.delete()
        return Response({'answer': f'{answer_pk} deleted'}, status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)