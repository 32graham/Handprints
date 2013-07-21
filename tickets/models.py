from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class TicketState(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Ticket(models.Model):
    title = models.CharField(max_length=50)
    company = models.ForeignKey(Company)
    state = models.ForeignKey(TicketState)

    def __unicode__(self):
        return self.title
