
from django.urls import path ,include
from . import views


urlpatterns = [
    
   path('all',views.job_list,name="list"),
   path('add',views.add_job,name="addjob"),

   path('job_details/<str:slug>',views.job_details,name="job_deta"),

    
]
