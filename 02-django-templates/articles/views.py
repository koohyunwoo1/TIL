# import random
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'articles/index.html')


# def dinner(request):
#     foods = [
#         '국밥',
#         '국수',
#         '카레',
#         '탕수육',
#     ]
#     picked = random.choice(foods)
#     return render(request, 'articles/dinner.html', )
