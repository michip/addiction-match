from django.urls import path, include
from .views import *
urlpatterns = [
    path('<int:id>/', get_profile),
    path('create', create_profile)
]