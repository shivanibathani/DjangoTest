# Generated by Django 4.1.7 on 2023-03-25 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_question_question_text_lower_choice_unique_choice'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='choice',
            name='unique_choice',
        ),
    ]