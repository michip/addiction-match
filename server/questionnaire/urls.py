
from django.shortcuts import render

# Create your views here.

from django.urls import path, include
from .views import *
urlpatterns = [
    path('answer', process_answer)
]