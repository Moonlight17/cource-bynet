from django.db import models
import datetime


class Participants(models.Model):
    Name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class ListEmails(models.Model):
    user = models.ForeignKey(Participants, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)


class Aggregate(models.Model):
    participant = models.ForeignKey(Participants, on_delete=models.CASCADE)
    time_on_less = models.IntegerField("Time On Lesson")
    date = models.DateField("Date", default=datetime.date.today)
