from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class ProductVersion(models.Model):
    major = models.IntegerField()
    minor = models.IntegerField()
    revision = models.IntegerField(blank=True, null=True)
    build = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey(Product)

    def __unicode__(self):
        return self.product.name + ' ' + '.'.join((
            str(self.major),
            str(self.minor)))


class Company(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    product_versions = models.ManyToManyField(
        ProductVersion,
        blank=True,
        related_name='companies')

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
    created_date_time = models.DateTimeField()
    user_created = models.ForeignKey(User, related_name='created_tickets')
    tier = models.ForeignKey(Tier)
    status = models.ForeignKey(Status)
    assignees = models.ManyToManyField(User, blank=True)
    product = models.ForeignKey(ProductVersion, blank=True, null=True)
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

    def __unicode__(self):
        return self.comment
