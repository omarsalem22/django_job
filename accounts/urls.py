from django.urls import path ,include
from . import views


urlpatterns = [
    
   path('signup',views.signup,name="signup"),
   path('profile',views.profile,name='profile'),
   path('profile_edit',views.profile_edit,name='profile_edit'),
   



    
]
