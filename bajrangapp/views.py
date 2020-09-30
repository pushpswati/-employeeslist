from django.shortcuts import render
from django.http import HttpResponse
from bajrangapp.serializers import employeesSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employees


class employeesList(APIView):

    def get(self,request):
        employee1= employees.objects.all()
        serializer=employeesSerializers(employee1,many=True)
        return  Response(serializer.data)
    def post(self,request):
        serializer = employeesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

