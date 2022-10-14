
from msilib.schema import Class
import re
from sre_constants import CATEGORY
from unicodedata import category, name
from django.db import models

# Create your models here.
class job(models.Model):
    JOP_TYPE=(
        ('Full Time','Full Time'),
        ('Part Time','Part Time'),
    )
    title=models.CharField(max_length=100)
    job_type=models.CharField(max_length=20 ,choices=JOP_TYPE )
    description=models.TextField(max_length=500,default='')
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    category= models.ForeignKey('Category',on_delete=models.CASCADE ,null=True) 


    def __str__(self) -> str:
        return self.title 

class Category(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name




    
