from django.shortcuts import render
from.models import *

# Create your views here.
def job_list(reqeust):
    jobs=job.objects.all()
    context={"jobs":jobs}
    return

def job_details(request,id):
    pass