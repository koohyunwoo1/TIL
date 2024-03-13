from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'todos/index.html')

def create_todo(request):
    return render(request, 'todos/create_todo.html')