from django.shortcuts import render, redirect
from .models import Garage

# Create your views here.
def index(request):
    # 전체 차고지 정보
    # Model.manage.querySet API()
    # all 메서드 호출 결과를 garages 변수에 할당하고,

    garages = Garage.objects.all()
    context = {
        'garages' : garages
    }
    return render(request, 'garages/index.html')

def new(request):
    return render(request, 'garages/new.html')

def create(request):
    # 사용자의 요청 정보를 모두 담고 있는 request를 사용해서
    # 사용자가 POST 방식으로 보내온 데이터들
    '''
        request.POST => {
            'location ' : value
            'capacity' : value
            'is_parking_avaliable' : value
            'opening_time' : value
            'closing_time ' : value
        }
    '''
    location = request.POST.get('location')
    capacity = request.POST.get('capacity')
    is_parking_avaliable = request.POST.get('is_parking_avaliable')
    opening_time = request.POST.get('opening_time')
    closing_time = request.POST.get('closing_time')

    garage = Garage(location=location,capacity=capacity,is_parking_avaliable=is_parking_avaliable,opening_time=opening_time,closing_time=closing_time)
    garage.save()
    return redirect('garages:index')


def detail(request, garage_pk):
    # pk 값이 사용자가 요청보내온 pk 값을 가지고 있는 데이터 하나
    garage = Garage.objects.get(pk = garage_pk)
    context = {
        'garage' : garage
    }

    return render(request, 'garages/detail.html', context)