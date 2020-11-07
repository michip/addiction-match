from django.db import models
from profiles.models import Profile


class Answer(models.Model):
    value = models.CharField(max_length=400)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return f"Answer {self.value} for {self.question.text}"

    def to_json(self):
        return {
            "pk": self.pk,
            "value": self.value,
        }


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

    def to_json(self):
        obj = {
            "pk": self.pk,
            "text": self.text,
            "style": self.style,
        }

        if self.style == "slider":
            obj["min_value"] = 0
            obj["max_value"] = 10
            obj["step"] = 1
        else:
            obj["answers"] = [a.to_json() for a in self.answers.all()]

        return obj


class QuestionnaireResult(models.Model):
    answers = models.ManyToManyField(Answer)
    profile = models.OneToOneField(Profile,
                                   on_delete=models.CASCADE,
                                   related_name='questionnaire_result')

    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def to_json(self):
        return {
            "answers": list(map(lambda x: x.to_json(), self.answers.all())),
            "profile": self.profile.to_json()
        }