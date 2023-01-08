from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serialzers import *

from rest_framework import status


@api_view(['GET'])
def view(request):
    if request.method == 'GET':
        list = CreateTodo.objects.all()
        serializer = TodoSerializer(list, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def create(request):
    if request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("/")
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def do(request, id):

    list = CreateTodo.objects.get(id=id)
    if request.method == 'GET':
        serializer = TodoSerializer(list)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TodoSerializer(list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










# Create your views here.
