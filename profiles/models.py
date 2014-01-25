from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from companies.models import Company


class Theme(models.Model):
    name = models.CharField(max_length=50)
    html = models.CharField(max_length=300)

    def __unicode__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User)
    company = models.ForeignKey(Company)
    theme = models.ForeignKey(Theme, default=1)

    def __unicode__(self):
        return self.user.get_full_name()

    def open_assignments(self):
        return self.assignments.filter(status__name='Open')

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.pk)])
