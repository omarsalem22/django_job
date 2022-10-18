
from django.utils.text import slugify
from distutils.command.upload import upload
from msilib.schema import Class
import re
from sre_constants import CATEGORY
from unicodedata import category, name
from django.db import models

# Create your models here.

def image_upload(instance,filename):
    imagename,extension=filename.split(".")
    return "jobs/%s.%s"%(instance.title,extension)
    
class job(models.Model):
    JOP_TYPE=(
        ('Full Time','Full Time'),
        ('Part Time','Part Time'),
    )
    title=models.CharField(max_length=100)
    image= models.ImageField(upload_to=image_upload,null=True)
    job_type=models.CharField(max_length=20 ,choices=JOP_TYPE )
    description=models.TextField(max_length=500,default='')
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    category= models.ForeignKey('Category',on_delete=models.CASCADE ,null=True) 
    slug=models.SlugField(blank=True,null=True)
  


    def save(self,*args,**kwargs):
        self.slug=slugify( self.title)
        super(job,self).save(*args,**kwargs)
    def __str__(self) -> str:
        return self.title 

class Category(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name




    
