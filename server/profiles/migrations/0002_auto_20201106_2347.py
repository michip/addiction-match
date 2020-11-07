# Generated by Django 3.1.3 on 2020-11-06 23:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthday_year',
            field=models.IntegerField(default=1990),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default=None, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.IntegerField(choices=[(0, 'male'), (1, 'female'), (2, 'other')], default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='matching_preference',
            field=models.IntegerField(choices=[(0, 'no_match'), (1, 'mentor')], default=1),
        ),
        migrations.AddField(
            model_name='profile',
            name='picture_url',
            field=models.CharField(default=None, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='story',
            field=models.CharField(default=None, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
