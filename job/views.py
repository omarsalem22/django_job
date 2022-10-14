from multiprocessing import context
from django.shortcuts import render
from.models import *

# Create your views here.
def job_list(reqeust):
    job_list=job.objects.all()
    context={"jobs":job_list}
    return render(reqeust,'job/job_list.html',context)

def job_details(reqeust,id):
    job_detail=job.objects.get(id=id)
    context={"details":job_detail}
    return render(reqeust,'job/job_details.html',context)


