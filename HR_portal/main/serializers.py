from rest_framework.serializers import ModelSerializer
from .models import Employee, Guarantor

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class GuarantorSerializer(ModelSerializer):
    class Meta:
        model = Guarantor
        fields = '__all__'
        


