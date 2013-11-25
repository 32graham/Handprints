# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Company'
        db.delete_table(u'tickets_company')

        # Removing M2M table for field product_versions on 'Company'
        db.delete_table(db.shorten_name(u'tickets_company_product_versions'))

        # Deleting model 'ProductVersion'
        db.delete_table(u'tickets_productversion')

        # Deleting model 'Product'
        db.delete_table(u'tickets_product')


        # Changing field 'Ticket.product'
        db.alter_column(u'tickets_ticket', 'product_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['companies.Product'], null=True))

        # Changing field 'Ticket.company'
        db.alter_column(u'tickets_ticket', 'company_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['companies.Company']))

    def backwards(self, orm):
        # Adding model 'Company'
        db.create_table(u'tickets_company', (
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'tickets', ['Company'])

        # Adding M2M table for field product_versions on 'Company'
        m2m_table_name = db.shorten_name(u'tickets_company_product_versions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('company', models.ForeignKey(orm[u'tickets.company'], null=False)),
            ('productversion', models.ForeignKey(orm[u'tickets.productversion'], null=False))
        ))
        db.create_unique(m2m_table_name, ['company_id', 'productversion_id'])

        # Adding model 'ProductVersion'
        db.create_table(u'tickets_productversion', (
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tickets.Product'])),
            ('major', self.gf('django.db.models.fields.IntegerField')()),
            ('build', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('minor', self.gf('django.db.models.fields.IntegerField')()),
            ('revision', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'tickets', ['ProductVersion'])

        # Adding model 'Product'
        db.create_table(u'tickets_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'tickets', ['Product'])


        # Changing field 'Ticket.product'
        db.alter_column(u'tickets_ticket', 'product_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tickets.Product'], null=True))

        # Changing field 'Ticket.company'
        db.alter_column(u'tickets_ticket', 'company_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tickets.Company']))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'companies.company': {
            'Meta': {'object_name': 'Company'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'product_versions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'companies'", 'blank': 'True', 'to': u"orm['companies.ProductVersion']"})
        },
        u'companies.product': {
            'Meta': {'object_name': 'Product'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'companies.productversion': {
            'Meta': {'object_name': 'ProductVersion'},
            'build': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major': ('django.db.models.fields.IntegerField', [], {}),
            'minor': ('django.db.models.fields.IntegerField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['companies.Product']"}),
            'revision': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'tickets.department': {
            'Meta': {'object_name': 'Department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'tickets.status': {
            'Meta': {'object_name': 'Status'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'tickets.ticket': {
            'Meta': {'object_name': 'Ticket'},
            'assignees': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'assignments'", 'blank': 'True', 'to': u"orm['auth.User']"}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['companies.Company']"}),
            'created_date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['companies.Product']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.Status']"}),
            'tier': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.Tier']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_changed': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_tickets'", 'to': u"orm['auth.User']"})
        },
        u'tickets.ticketassigneeadded': {
            'Meta': {'object_name': 'TicketAssigneeAdded'},
            'assignee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'change_set': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'added_assignees'", 'to': u"orm['tickets.TicketAssigneeChangeSet']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'tickets.ticketassigneechangeset': {
            'Meta': {'object_name': 'TicketAssigneeChangeSet'},
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ticket': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assignee_changes'", 'to': u"orm['tickets.Ticket']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"})
        },
        u'tickets.ticketassigneeremoved': {
            'Meta': {'object_name': 'TicketAssigneeRemoved'},
            'assignee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'change_set': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'removed_assignees'", 'to': u"orm['tickets.TicketAssigneeChangeSet']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'tickets.ticketcomment': {
            'Meta': {'object_name': 'TicketComment'},
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ticket': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': u"orm['tickets.Ticket']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'tickets.ticketstatuschange': {
            'Meta': {'object_name': 'TicketStatusChange'},
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['tickets.Status']"}),
            'old_status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['tickets.Status']"}),
            'ticket': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'status_changes'", 'to': u"orm['tickets.Ticket']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'tickets.tickettierchange': {
            'Meta': {'object_name': 'TicketTierChange'},
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_tier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['tickets.Tier']"}),
            'old_tier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['tickets.Tier']"}),
            'ticket': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tier_changes'", 'to': u"orm['tickets.Ticket']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'tickets.tier': {
            'Meta': {'object_name': 'Tier'},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.Department']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['tickets']