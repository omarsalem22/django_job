
from django.urls import path ,include
from . import views
from . import api


urlpatterns = [
    
   path('all',views.job_list,name="list"),
   path('add',views.add_job,name="addjob"),

   path('job_details/<str:slug>',views.job_details,name="job_deta"),
   ###Api
  path('jobs/',api.job_list_api,name="joblistapi"),
  path('job/<int:id>',api.job_detail_api,name="job_detail_api"),

  #classapi
  path('jobsv2/',api.Job_listapi.as_view(),name="Job_listapi"),
  path('JobDetialv2/<int:id>',api.JobDetial.as_view(),name="JobDetial"),


  





   
]
