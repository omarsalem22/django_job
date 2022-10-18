from multiprocessing import context
from django.shortcuts import render
from.models import *
from django.core.paginator import Paginator

# Create your views here.
def job_list(request):
    job_list=job.objects.order_by('title')
    paginator = Paginator(job_list, 1) # Show 25 contacts per page.
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)
  
    context={"jobs":page_obj}
    return render(request,'job/job_list.html',context)

def job_details(request,slug):
    job_detail=job.objects.get(slug=slug)
    context={"details":job_detail}
    return render(request,'job/job_details.html',context)


