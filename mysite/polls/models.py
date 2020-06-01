# https://docs.djangoproject.com/es/3.0/intro/tutorial02/
import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

# Has a quiestion and a publicarion date

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# Has two fields, the text of the choice and a vote tally
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
