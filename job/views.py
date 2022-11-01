from multiprocessing import context
from django.shortcuts import render ,redirect
from.models import *
from django.core.paginator import Paginator
from .forms import *
from  django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter
# Create your views here.
def job_list(request):
    job_list=Job.objects.order_by('title')

    myfilter=JobFilter(request.GET,queryset=job_list)
    job_list=myfilter.qs

    paginator = Paginator(job_list, 3) # Show 3 contacts per page.
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)
    # filters
  
    context={"jobs":page_obj,'myfilter':myfilter}
    return render(request,'job/job_list.html',context)

def job_details(request,slug):
    job_detail=Job.objects.get(slug=slug)
    if request.method=="POST":
         form=Applyform(request.POST,request.FILES)
         if form.is_valid():
            myform=form.save(commit=False)
            myform.job=job_detail
            myform.save()


    else:
        form=Applyform()    
    context={"details":job_detail,'form':form}
    return render(request,'job/job_details.html',context)

@login_required
def add_job(request):
    if request.method=="POST":
       form=Job_form(request.POST,request.FILES)
       if form.is_valid():
        myform=form.save(commit=False)
        myform.owner=request.user
        myform.save()
        return redirect (reverse('list'))
    else:
        form=Job_form()
    context={'form':form}   
    return render(request,'job/add_job.html',context)