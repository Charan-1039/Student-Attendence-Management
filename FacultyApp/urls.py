from django.contrib import admin
from django.urls import path,include
from FacultyApp import views


urlpatterns = [
    path('Faculty/',views.FacultyInterface,name='Faculty'),
]
