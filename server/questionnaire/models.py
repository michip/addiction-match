from django.db import models
from profiles.models import Profile


class Answer(models.Model):
    value = models.CharField(max_length=400)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return f"Answer {self.value} for {self.question.text}"


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

    order = models.FloatField(default=1)
    follows_after_answer = models.ForeignKey(Answer, on_delete=models.SET_NULL,
                                             null=True, blank=True, default=None, related_name='followup_questions')


    def __str__(self):
        return f"{self.text} ({self.style})"


class QuestionnaireResult:
    answers = models.ManyToManyField(Answer)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
