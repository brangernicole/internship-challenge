"""
URL configuration for the API app
"""
from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('lcm/', views.calculate_lcm, name='calculate_lcm'),
]
