from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    desciption=models.CharField(max_length=100, blank=True, null=True)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Voter(models.Model):
    voter=models.OneToOneField(User, on_delete=models.CASCADE)
