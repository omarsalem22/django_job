

from django.utils.text import slugify
from distutils.command.upload import upload
from msilib.schema import Class

from sre_constants import CATEGORY
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def image_upload(instance,filename):
    imagename,extension=filename.split(".")
    return "jobs/%s.%s"%(instance.title,extension)
    
class Job(models.Model):
    JOP_TYPE=(
        ('Full Time','Full Time'),
        ('Part Time','Part Time'),
    )
    owner=models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE)
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
        super(Job,self).save(*args,**kwargs)
    def __str__(self) -> str:
        return self.title 

class Category(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name
class Apply(models.Model):
    job=models.ForeignKey(Job,related_name='apply_job',on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    website=models.URLField()
    cv=models.FileField(upload_to='apply/')
    cover_letter=models.TextField(max_length=200)
    created_at=models.DateTimeField(auto_now=True)

    
    def __str__(self) -> str:
        return self.name

    





    
