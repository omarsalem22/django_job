###get data from model , convert it to jeson
from dataclasses import field, fields
from pyexpat import model
from rest_framework import  serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
   class Meta:
    model=Job
    fields='__all__'
    