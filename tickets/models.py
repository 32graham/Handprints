from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from simple_history.models import HistoricalRecords


class Company(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Tier(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department)

    def __unicode__(self):
        return self.name


class Ticket(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    company = models.ForeignKey(Company)
    is_blocker = models.BooleanField(verbose_name=u'blocker')
    tier = models.ForeignKey(Tier)
    status = models.ForeignKey(Status)
    assignee = models.ForeignKey(User, related_name='assignments')
    changed_by = models.ForeignKey(User, related_name='ticket_changes')
    history = HistoricalRecords()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tickets.views.ticket', args=[str(self.pk)])


class TicketComment(models.Model):
    ticket = models.ForeignKey(Ticket)
    comment = models.TextField()
    date_time = models.DateTimeField()
    user = models.ForeignKey(User)
    is_public = models.BooleanField()
    attachment = models.FileField(upload_to='attachment', null=True, blank=True)

    def __unicode__(self):
        return self.comment
