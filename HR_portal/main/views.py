from django.shortcuts import render
#from rest_framework. import  
from .models import Employee
from rest_framework.viewsets import ModelViewSet
from .serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class AllEmployees(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]


    
