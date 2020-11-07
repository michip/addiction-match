from django.urls import path, include
from .views import *
urlpatterns = [
    path('get', ProfileView.as_view()),
    path('create', create_profile),
    path('scrape', scrape_profiles)
]