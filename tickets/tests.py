from datetime import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.timezone import utc
from .models import Ticket, Company, Tier, Department, Status, TicketComment
from .views import TicketChange

class TicketsViewsTestCase(TestCase):

    def setUp(self):
        company = Company.objects.create(name='company', notes='notes')
        department = Department.objects.create(name='department')
        tier = Tier.objects.create(name='tier', department=department)
        tier2 = Tier.objects.create(name='tier2', department=department)
        status = Status.objects.create(name='status')
        status2 = Status.objects.create(name='status2')
        user = User.objects.create_user(username='username', password='password')
        user2 = User.objects.create_user(username='username2', password='password2')
        ticket = Ticket.objects.create(
            title='title',
            description='description',
            company=company,
            is_blocker=False,
            tier=tier,
            status=status,
            assignee=user,
            changed_by=user,
        )
        comment = TicketComment.objects.create(
            ticket=ticket,
            comment='comment',
            date_time=datetime.utcnow().replace(tzinfo=utc),
            user=user,
            is_public=False,
        )
        ticket.tier = tier2
        ticket.status = status2
        ticket.assignee = user2
        ticket.save()
        ticket.tier = tier
        ticket.status = status
        ticket.assignee = user
        ticket.save()



    def test_index(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)


    def test_ticket(self):
        self.client.login(username='username', password='password')
        resp = self.client.get(reverse('ticket', args=[1]))
        self.assertEqual(resp.status_code, 200)
        self.assertIn('company', resp.content)


    def test_ticket_does_not_exist(self):
        self.client.login(username='username', password='password')
        resp = self.client.get(reverse('ticket', args=[100]))
        self.assertEqual(resp.status_code, 404)


    def test_ticket_access_denied_without_login(self):
        resp = self.client.get(reverse('ticket', args=[1]))
        self.assertEqual(resp.status_code, 302)


    def test_status(self):
        self.client.login(username='username', password='password')
        resp = self.client.get(reverse('status', args=[1]))
        self.assertEqual(resp.status_code, 200)
        self.assertIn('status', resp.content)


    def test_status_access_denied_without_login(self):
        resp = self.client.get(reverse('status', args=[1]))
        self.assertEqual(resp.status_code, 302)


    def test_tier(self):
        self.client.login(username='username', password='password')
        resp = self.client.get(reverse('tier', args=[1]))
        self.assertEqual(resp.status_code, 200)
        self.assertIn('tier', resp.content)


    def test_tier_access_denied_without_login(self):
        resp = self.client.get(reverse('tier', args=[1]))
        self.assertEqual(resp.status_code, 302)


    def test_company(self):
        self.client.login(username='username', password='password')
        resp = self.client.get(reverse('company', args=[1]))
        self.assertEqual(resp.status_code, 200)
        self.assertIn('company', resp.content)


    def test_company_access_denied_without_login(self):
        resp = self.client.get(reverse('company', args=[1]))
        self.assertEqual(resp.status_code, 302)


    def test_ticket_good_edit(self):
        self.client.login(username='username', password='password')
        ticket = Ticket.objects.get(pk=1)
        self.assertEqual(ticket.tier.pk, 1)
        resp = self.client.post(reverse('ticket', args=[1]), {
                'tier': 1,
                'status': 1,
                'assignee': 1,
            }
        )
        self.assertEqual(resp.status_code, 302)


    def test_comment_good(self):
        self.client.login(username='username', password='password')
        resp = self.client.post(reverse('comment', args=[1]), {
                'comment': 'new comment',
                'attachment': '',
            }
        )
        self.assertEqual(resp.status_code, 302)


    def test_new_ticket(self):
        self.client.login(username='username', password='password')
        resp = self.client.get(reverse('new_ticket'))
        self.assertEqual(resp.status_code, 200)


    def test_new_ticket_good(self):
        self.client.login(username='username', password='password')
        resp = self.client.post(reverse('new_ticket'), {
                'title': 'title',
                'description': 'description',
                'company': 1,
                'assignee': 1,
                'tier': 1,
                'status': 1,
                'is_blocker': 'True',
            }
        )
        self.assertEqual(resp.status_code, 302)


    def test_company_unicode(self):
        company = Company.objects.get(pk=1)
        self.assertEqual(company.__unicode__(), 'company')


    def test_status_unicode(self):
        status = Status.objects.get(pk=1)
        self.assertEqual(status.__unicode__(), 'status')


    def test_tier_unicode(self):
        tier = Tier.objects.get(pk=1)
        self.assertEqual(tier.__unicode__(), 'tier')


    def test_department_unicode(self):
        department = Department.objects.get(pk=1)
        self.assertEqual(department.__unicode__(), 'department')


    def test_ticket_unicode(self):
        ticket = Ticket.objects.get(pk=1)
        self.assertEqual(ticket.__unicode__(), 'title')


    def test_ticketComment_unicode(self):
        ticketComment = TicketComment.objects.get(pk=1)
        self.assertEqual(ticketComment.__unicode__(), 'comment')


    def test_ticket_absolute_url(self):
        ticket = Ticket.objects.get(pk=1)
        self.assertEqual(ticket.get_absolute_url(), reverse('ticket', args=[ticket.pk]))


    def test_ticket_change(self):
        date = datetime.utcnow().replace(tzinfo=utc)
        ticket_change = TicketChange(
            field_name='field_name',
            old_value='old_value',
            new_value='new_value',
            date_time=date,
        )
        self.assertEqual(ticket_change.field_name, 'field_name')
        self.assertEqual(ticket_change.old_value, 'old_value')
        self.assertEqual(ticket_change.new_value, 'new_value')
        self.assertEqual(ticket_change.date_time, date)
