from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AllEmployees
 
router = DefaultRouter()
router.register(r'employees', AllEmployees)

urlpatterns = [
    path('', include(router.urls)),
]
