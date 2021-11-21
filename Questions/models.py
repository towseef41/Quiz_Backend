from django.db import models
from django.db.models.base import ModelState

# Create your models here.

class Round(models.Model):
    round_number = models.CharField(max_length=20)

class Question(models.Model):
    belongs_to = models.ForeignKey(Round, on_delete=models.CASCADE)
    question = models.TextField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()

class Task(models.Model):
    description = models.TextField()
    meme = models.ImageField(upload_to = 'memes/')
    used = models.BooleanField(default=False)