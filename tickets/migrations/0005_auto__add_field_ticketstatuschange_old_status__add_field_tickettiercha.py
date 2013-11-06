# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TicketStatusChange.old_status'
        db.add_column(u'tickets_ticketstatuschange', 'old_status',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='+', to=orm['tickets.Status']),
                      keep_default=False)

        # Adding field 'TicketTierChange.old_tier'
        db.add_column(u'tickets_tickettierchange', 'old_tier',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='+', to=orm['tickets.Tier']),
                      keep_default=False)

        # Adding field 'Ticket.user_changed'
        db.add_column(u'tickets_ticket', 'user_changed',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='+', to=orm['auth.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TicketStatusChange.old_status'
        db.delete_column(u'tickets_ticketstatuschange', 'old_status_id')

        # Deleting field 'TicketTierChange.old_tier'
        db.delete_column(u'tickets_tickettierchange', 'old_tier_id')

        # Deleting field 'Ticket.user_changed'
        db.delete_column(u'tickets_ticket', 'user_changed_id')


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
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'product_versions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'companies'", 'blank': 'True', 'to': u"orm['tickets.ProductVersion']"})
        },
        u'tickets.department': {
            'Meta': {'object_name': 'Department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'tickets.product': {
            'Meta': {'object_name': 'Product'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'tickets.productversion': {
            'Meta': {'object_name': 'ProductVersion'},
            'build': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major': ('django.db.models.fields.IntegerField', [], {}),
            'minor': ('django.db.models.fields.IntegerField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.Product']"}),
            'revision': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'tickets.status': {
            'Meta': {'object_name': 'Status'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'tickets.ticket': {
            'Meta': {'object_name': 'Ticket'},
            'assignees': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.Company']"}),
            'created_date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.ProductVersion']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.Status']"}),
            'tier': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.Tier']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_changed': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_tickets'", 'to': u"orm['auth.User']"})
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