from django.urls import path, include
from .views import *


urlpatterns = [
    path('<int:id>/', get_conversation),
    path('create', create_conversation),
    path('messages/send', send_message),
    path('messages/get-new', get_new_messages),
]