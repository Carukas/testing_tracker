from django.contrib import admin
from django.urls import path
from . import views

app_name='testing'

urlpatterns = [
    
    path('', views.start, name="start"),
    path('valdzios_nurodymai', views.valdzios_nurodymai, name="valdzios_nurodymai"),
    path('sarasas', views.sarasas, name="sarasas"),
    path('valdzios_nurodymai_enter', views.valdzios_nurodymai_enter, name="valdzios_nurodymai_enter"),
    path('valdzios_nurodymai_update', views.valdzios_nurodymai_update, name="valdzios_nurodymai_update"),
    path('enter_person', views.enter_person, name="enter_person"),
    path('update_person', views.update_person, name="update_person"),


   
]