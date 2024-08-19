from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm
# Create your views here.
def index(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'reservations/index.html', context)

def new(request):
    form = ReservationForm()
    context = {
        'form' : form,
    }
    return render(request, 'reservations/new.html', context)

def create(request):
    form = ReservationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('reservations:index')
    context = {
        'form': form
    }
    return render(request, 'reservations/new.html', context)
        
