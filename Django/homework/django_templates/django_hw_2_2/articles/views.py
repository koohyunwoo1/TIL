from django.shortcuts import render

# Create your views here.
def send(request):
    return render(request, 'articles/send.html')

def receive(request):
    message = request.GET.get('message')
    context = {
        'message': message
    }
    return render(request, 'articles/receive.html', context)