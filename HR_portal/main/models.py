from django.db import models

from django.core.validators import RegexValidator

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,10}$',  # accepts +<country code><phone number>
        message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.",
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True, unique=True)  # accepts '+999999999'
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

    def __str__(self):
        return self.name + " " + self.jobs

class Guarantor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,10}$',  # accepts +<country code><phone number>
        message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.",
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True, unique=True)  # accepts '+999999999'
    address = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    id_no= models.CharField(max_length=15, validators=[RegexValidator(r'^[a-zA-Z0-9]*$', 'Only alphanumeric characters are allowed.')])
    
    def __str__(self):
        return self.name + " " + self.phone_number
    
