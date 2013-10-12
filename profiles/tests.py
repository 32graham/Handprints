from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class TicketsViewsTestCase(TestCase):

    def setUp(self):
        User.objects.create_user(username='username', password='password')


    def test_profile(self):
        self.client.login(username='username', password='password')
        resp = self.client.get(reverse('profile', args=[1]))
        self.assertEqual(resp.status_code, 200)
