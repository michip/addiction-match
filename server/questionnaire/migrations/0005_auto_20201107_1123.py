# Generated by Django 3.1.3 on 2020-11-07 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0004_auto_20201107_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='followup_question',
        ),
        migrations.AddField(
            model_name='question',
            name='follows_after_answer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='followup_questions', to='questionnaire.answer'),
        ),
    ]