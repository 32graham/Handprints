from django.contrib.auth.models import User
from tickets.models import Company
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User)
    company = models.ForeignKey(Company)

    def __unicode__(self):
        items = (str(self.user), str(self.company))
        return ' - '.join(items)
