from django.urls import path
from . import views

app_name = "colormean"

urlpatterns = [
    path('',views.primarycolor,name='primarycolor'),
    path('secondarycolor/',views.secondarycolor,name='secondarycolor'),
    path('specialcolor/',views.specialcolor,name='specialcolor')
]