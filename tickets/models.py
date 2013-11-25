from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from companies.models import Product, Company


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
    created_date_time = models.DateTimeField()
    user_created = models.ForeignKey(User, related_name='created_tickets')
    tier = models.ForeignKey(Tier)
    status = models.ForeignKey(Status)
    assignees = models.ManyToManyField(User, blank=True, related_name='assignments')
    product = models.ForeignKey(Product, blank=True, null=True)
    user_changed = models.ForeignKey(User, related_name='+')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tickets.views.ticket', args=[str(self.pk)])


class TicketTierChange(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='tier_changes')
    date_time = models.DateTimeField()
    new_tier = models.ForeignKey(Tier, related_name='+')
    old_tier = models.ForeignKey(Tier, related_name='+')
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user.get_full_name() + ' ' + self.new_tier.__unicode__()

    class Meta:
      get_latest_by = 'date_time'


class TicketStatusChange(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='status_changes')
    date_time = models.DateTimeField()
    new_status = models.ForeignKey(Status, related_name='+')
    old_status = models.ForeignKey(Status, related_name='+')
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user.get_full_name() + ' ' + self.new_status.name

    class Meta:
      get_latest_by = 'date_time'


class TicketComment(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='comments')
    date_time = models.DateTimeField()
    comment = models.TextField()
    user = models.ForeignKey(User)
    attachment = models.FileField(upload_to='attachment', null=True, blank=True)
    is_public = models.BooleanField()

    def __unicode__(self):
        return self.comment


class TicketAssigneeChangeSet(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='assignee_changes')
    date_time = models.DateTimeField()
    user = models.ForeignKey(User, related_name='+')

    def __unicode__(self):
        added = ", ".join(str(assignee) for assignee in self.added_assignees.all())
        removed = ", ".join(str(assignee) for assignee in self.removed_assignees.all())

        string = 'Assignees'

        if len(added) > 0:
            string = string + ' added ' + added
        if len(removed) > 0:
            string = string + ' removed ' + removed

        return string


class TicketAssigneeAdded(models.Model):
    change_set = models.ForeignKey(TicketAssigneeChangeSet, related_name='added_assignees')
    assignee = models.ForeignKey(User)

    def __unicode__(self):
        return self.assignee.get_full_name()


class TicketAssigneeRemoved(models.Model):
    change_set = models.ForeignKey(TicketAssigneeChangeSet, related_name='removed_assignees')
    assignee = models.ForeignKey(User)

    def __unicode__(self):
        return self.assignee.get_full_name()
