from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from companies.models import Company
from .models import Profile


class TicketsViewsTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='username', password='password')
        user.is_staff = True
        user.save()
        company = Company.objects.create(name='company')
        Profile.objects.create(company=company, user=user)

    def test_profile(self):
        self.client.login(username='username', password='password')
        resp = self.client.get(reverse('profile', args=(1,)))
        self.assertEqual(resp.status_code, 200)
