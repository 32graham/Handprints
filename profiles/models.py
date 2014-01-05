from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from tickets.models import Company
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User)
    company = models.ForeignKey(Company)

    def __unicode__(self):
        return self.user.get_full_name()

    def open_assignments(self):
        return self.assignments.filter(status__name='Open')

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.pk)])
