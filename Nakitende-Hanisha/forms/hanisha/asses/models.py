
# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.
class BioData(models.Model):
    first_name = models.CharField(max_length=100,null=False, blank=False)
    last_name = models.CharField(max_length=100,null=False, blank=False)
    date_of_birth = models.DateField(
        help_text='Enter your date of birth in YY/MM/DD format.'
    )

    gender= models.CharField(max_length=30,choices=[('m', 'male'),('f','female')])

    def _str_(self):
        return self.first_name
class Location(models.Model):
    country= models.CharField(max_length=100,null=False,blank=False)
    state= models.CharField(max_length=100,null=False,blank=False)
    town= models.CharField(max_length=100,null=False,blank=False)
    zip_code= models.CharField(max_length=100,null=False,blank=False)
    
    def _str_(self):
        return self.country
    
class Contact(models.Model):
    phone_number = models.CharField(max_length=100,null=False, blank=False)
    phone_number2 = models.CharField(max_length=100,null=False, blank=False)
    email=models.EmailField(unique=True)

    def _str_(self):
        return self.phone_number