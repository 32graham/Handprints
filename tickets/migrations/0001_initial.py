# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Company'
        db.create_table(u'tickets_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'tickets', ['Company'])

        # Adding model 'Status'
        db.create_table(u'tickets_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'tickets', ['Status'])

        # Adding model 'Department'
        db.create_table(u'tickets_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'tickets', ['Department'])

        # Adding model 'Tier'
        db.create_table(u'tickets_tier', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tickets.Department'])),
        ))
        db.send_create_signal(u'tickets', ['Tier'])

        # Adding model 'Ticket'
        db.create_table(u'tickets_ticket', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tickets.Company'])),
            ('created_date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('tier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tickets.Tier'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tickets.Status'])),
        ))
        db.send_create_signal(u'tickets', ['Ticket'])

        # Adding model 'TicketTierChange'
        db.create_table(u'tickets_tickettierchange', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ticket', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tier_changes', to=orm['tickets.Ticket'])),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('new_tier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tickets.Tier'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'tickets', ['TicketTierChange'])

        # Adding model 'TicketStatusChange'
        db.create_table(u'tickets_ticketstatuschange', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ticket', self.gf('django.db.models.fields.related.ForeignKey')(related_name='status_changes', to=orm['tickets.Ticket'])),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('new_status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tickets.Status'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'tickets', ['TicketStatusChange'])

        # Adding model 'TicketComment'
        db.create_table(u'tickets_ticketcomment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ticket', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comments', to=orm['tickets.Ticket'])),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('attachment', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'tickets', ['TicketComment'])


    def backwards(self, orm):
        # Deleting model 'Company'
        db.delete_table(u'tickets_company')

        # Deleting model 'Status'
        db.delete_table(u'tickets_status')

        # Deleting model 'Department'
        db.delete_table(u'tickets_department')

        # Deleting model 'Tier'
        db.delete_table(u'tickets_tier')

        # Deleting model 'Ticket'
        db.delete_table(u'tickets_ticket')

        # Deleting model 'TicketTierChange'
        db.delete_table(u'tickets_tickettierchange')

        # Deleting model 'TicketStatusChange'
        db.delete_table(u'tickets_ticketstatuschange')

        # Deleting model 'TicketComment'
        db.delete_table(u'tickets_ticketcomment')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'tickets.company': {
            'Meta': {'object_name': 'Company'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'})
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
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.Company']"}),
            'created_date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.Status']"}),
            'tier': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.Tier']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'tickets.ticketcomment': {
            'Meta': {'object_name': 'TicketComment'},
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ticket': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': u"orm['tickets.Ticket']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'tickets.ticketstatuschange': {
            'Meta': {'object_name': 'TicketStatusChange'},
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.Status']"}),
            'ticket': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'status_changes'", 'to': u"orm['tickets.Ticket']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'tickets.tickettierchange': {
            'Meta': {'object_name': 'TicketTierChange'},
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_tier': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.Tier']"}),
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