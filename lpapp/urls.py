from django.urls import path
from . import views
app_name='lpapp'

urlpatterns = [
   path('',views.home,name='home'),
   path('service/',views.service,name='service'),
   path('teamupdate/', views.teamupdate, name='teamupdate'),
   path('profile/<int:pk>/', views.profile, name='profile'),
]