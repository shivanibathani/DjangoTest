from datetime import datetime, timezone
from django.db import models
from django.db.models.functions import Lower
from django.forms import ValidationError

# Create your models here.


class Question(models.Model):

    question_text = models.CharField(max_length=200)
    question_text_lower = models.CharField(max_length=200, unique=True)
    pub_date = models.DateTimeField('date published')

    def clean(self):
        self.question_text_lower = self.question_text.lower()
        existing_question = Question.objects.filter(
            question_text_lower=self.question_text_lower).exclude(pk=self.pk).first()
        if existing_question:
            raise ValidationError("A question with this text already exists.")

    def save(self, *args, **kwargs):
        self.clean()
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def clean(self):
        self.choice_text = self.choice_text.lower()
        existing_choice = Choice.objects.filter(
            question=self.question, choice_text=self.choice_text).exclude(pk=self.pk).first()
        if existing_choice:
            raise ValidationError(
                "A choice with this text already exists for this question.")

    def save(self, *args, **kwargs):
        self.clean()
        super(Choice, self).save(*args, **kwargs)

    def __str__(self):
        return self.choice_text
