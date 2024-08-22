from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Car
from .serializers import CarSerializer

@api_view(['GET'])
def getData(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addCar(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
