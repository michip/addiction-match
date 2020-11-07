from django.contrib import admin
from profiles.models import Profile
from questionnaire.models import QuestionnaireResult

# Register your models here.
admin.site.register(QuestionnaireResult)
admin.site.register(Profile)