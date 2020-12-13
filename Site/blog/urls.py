from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about, name='about'),
    path('kadoi/', views.kadoi, name='kadoi'),
    path('anakiklosima/', views.anakiklosima, name='anakiklosima'),
    path('antamoivi/', views.antamoivi, name='antamoivi'),

]