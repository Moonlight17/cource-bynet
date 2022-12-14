from django.db import models
import datetime
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html


class Participants(models.Model):
    class Status(models.TextChoices):
        Student = 'ST', _('Student')
        Employer = 'EM', _('Employer')

    Name = models.CharField(max_length=200)
    pub_date = models.DateField("Date", default=datetime.date.today, blank=True)
    status = models.CharField(max_length=2,
        choices=Status.choices,
        default=Status.Student,)

    def __str__(self):
        return self.Name


class ListEmails(models.Model):
    user = models.ForeignKey(Participants, related_name='participant', on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)

    # @admin.display
    def participant(self):
        return self.user.Name

    def __str__(self):
        return self.email


class Aggregate(models.Model):
    participant = models.ForeignKey(Participants, on_delete=models.CASCADE)
    time_on_less = models.IntegerField("Time On Lesson")
    date = models.DateField("Date", default=datetime.date.today)

    def __str__(self):
        return str(self.date)

    def all(self):
        return format_html(
            '<span style="color: #000;">{} --- {} </span>',
            self.participant.Name,
            self.time_on_less,
        )


class Lessons(models.Model):
    class Status(models.TextChoices):
        Online = 'On', _('Online')
        Offline = 'Of', _('Offline')

    meet_date = models.DateField('Lessons', default=datetime.date.today)
    durations = models.IntegerField("Lesson's Durations", default=0)
    status = models.CharField(max_length=2,
        choices=Status.choices,
        default=Status.Online,)



