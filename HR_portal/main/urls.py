from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AllEmployees,SingleEmployee, GuarantorsView, SingleGuarantor
 
router = DefaultRouter()
router.register(r'employees', AllEmployees)



urlpatterns = [
    path('', include(router.urls)),
    path('employee/<int:pk>/', SingleEmployee.as_view()),

    path('guarantors/', GuarantorsView.as_view()),
    path('guarantors/<int:pk>/', SingleGuarantor.as_view()),
    
]
