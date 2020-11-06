from django.db import models


class Profile(models.Model):
    first_name = models.fields.CharField(max_length=56)
