from django.db import models

# Create your models here.
class Info(models.Model):
    place=models.CharField(max_length=80, blank=True ,null=True)
    phone_number=models.CharField(max_length=15)
    email=models.EmailField(max_length=240)


   
       

    def __str__(self):
          return self.email
   
   