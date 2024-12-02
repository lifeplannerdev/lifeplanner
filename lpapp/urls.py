from django.urls import path
from . import views
app_name='lpapp'

urlpatterns = [
   path('',views.home,name='home'),
   path('service/',views.service,name='service'),
]