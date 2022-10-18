
from django.urls import path ,include
from . import views
apa_name='job'

urlpatterns = [
    
   path('all',views.job_list,name="list"),
   path('job_details/<str:slug>',views.job_details,name="job_deta")
    
]
