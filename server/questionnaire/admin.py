from django.contrib import admin
import django.forms as forms

from .models import Question, Answer

admin.site.register(Question)

admin.site.register(Answer)




