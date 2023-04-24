from django.shortcuts import render
#from rest_framework. import  
from .models import Employee, Guarantor
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import EmployeeSerializer, GuarantorSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.

class AllEmployees(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly | IsAuthenticated]

class GuarantorsView(ListCreateAPIView):
    queryset = Guarantor.objects.all()
    serializer_class = GuarantorSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

class SingleEmployee(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class SingleGuarantor(RetrieveUpdateDestroyAPIView):
    queryset = Guarantor.objects.all()
    serializer_class = GuarantorSerializer
    

    
