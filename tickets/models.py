from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class TicketState(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Tier(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name


class Ticket(models.Model):
    title = models.CharField(max_length=50)
    company = models.ForeignKey(Company)
    state = models.ForeignKey(TicketState)
    tier = models.ForeignKey(Tier)

    def __unicode__(self):
        return self.title

class TicketComment(models.Model):
    ticket = models.ForeignKey(Ticket)
    comment = models.TextField(max_length=1000)
    date_time = models.DateTimeField()

    def __unicode__(self):
        return self.comment
