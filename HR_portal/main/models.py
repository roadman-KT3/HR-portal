from django.db import models

from django.core.validators import RegexValidator

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField(validators=[RegexValidator(r'^[0-9]*$', 'Only numbers are allowed.')])
    address = models.CharField(max_length=100)
    id_number = models.CharField(max_length=15, validators=[RegexValidator(r'^[a-zA-Z0-9]*$', 'Only alphanumeric characters are allowed.')]) 
    ssnit_number = models.CharField(max_length=13, validators=[RegexValidator(r'^[a-zA-Z0-9]*$', 'Only alphanumeric characters are allowed.')])
    
    JOBS = (
        ('WH', 'Warehouse Manager'),
        ('WS', 'Warehouse Supervisor'),
        ('L', 'Loader'),
        ('DEO', 'Data Entry Officer'),
        ('D', 'Driver'),
        ('C', 'Cleaner'),

    )
    jobs = models.CharField(max_length= 3, choices=JOBS, default='WH')
    Guarantor = models.ForeignKey('Guarantor', on_delete=models.CASCADE)

class Guarantor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    id_no= models.CharField(max_length=13, validators=[RegexValidator(r'^[a-zA-Z0-9]*$', 'Only alphanumeric characters are allowed.')])
    
    def __str__(self):
        return self.name + " " + self.phone
    
