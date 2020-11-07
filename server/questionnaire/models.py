from django.db import models
from profiles.models import Profile


class Answer(models.Model):
    value = models.CharField(max_length=400)
    followup_question = models.ForeignKey('Question',
                                          on_delete=models.CASCADE, null=True, default=None, blank=True)

    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answers')


class Question(models.Model):
    STYLES = [
        ('radio', 'radio'),
        ('slider', 'slider'),
        ('autocomplete', 'autocomplete'),
        ('multiple', 'multiple')
    ]

    text = models.CharField(max_length=500)
    style = models.CharField(max_length=16,
                             choices=STYLES,
                             default='radio')


class QuestionnaireResult:
    answers = models.ManyToManyField(Answer)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
