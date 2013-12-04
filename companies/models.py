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

    def get_absolute_url(self):
        return reverse('company', args=[str(self.pk)])


class Company(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    product_versions = models.ManyToManyField(
        ProductVersion,
        blank=True,
        related_name='companies')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company', args=[str(self.pk)])
