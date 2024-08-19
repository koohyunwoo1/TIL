from django.shortcuts import render
from .models import Location, Station, Car
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import LocationSerializer, StationListSerializer, StationSerializer

# Create your views here.
@api_view(['POST'])
def location_create(request):
    if request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def station_create(request, location_pk):
    location = Location.objects.get(pk=location_pk)
    if request.method == 'POST':
        serializer = StationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(address=location)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def station_list(request):
    if request.method == 'GET':
        stations = Station.objects.all()
        serializer = StationListSerializer(stations, many=True)
        return Response(serializer.data)

@api_view(['GET', 'DELETE'])
def station_detail(request, station_pk):
    station = Station.objects.get(pk=station_pk)
    if request.method == 'GET':
        serializer = StationSerializer(station)
        return Response(serializer.data)
