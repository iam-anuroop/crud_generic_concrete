from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from .serializer import Studentserilaiser
from .models import Student
# from rest_framework.response import Response
# from rest_framework import status


class Student_create_view(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserilaiser
    
class Student_manage_view(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserilaiser
    
    


        


        




# Create your views here.
