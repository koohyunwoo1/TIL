from django.shortcuts import render

# Create your views here.

def introduce(request):

    context = {
        'username' : 'admin',
    }

    return render(request, 'introduce.html', context)