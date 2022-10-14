
from django.urls import path ,include
from . import views

urlpatterns = [
    
   path('',views.job_list,name="list"),
   path('job_details<int:id>',views.job_details,name="job_deta")
    
]
