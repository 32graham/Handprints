# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductVersion'
        db.create_table(u'companies_productversion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('major', self.gf('django.db.models.fields.IntegerField')()),
            ('minor', self.gf('django.db.models.fields.IntegerField')()),
            ('revision', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('build', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['companies.Product'])),
        ))
        db.send_create_signal(u'companies', ['ProductVersion'])

        # Adding model 'Product'
        db.create_table(u'companies_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'companies', ['Product'])

        # Adding model 'Company'
        db.create_table(u'companies_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'companies', ['Company'])

        # Adding M2M table for field product_versions on 'Company'
        m2m_table_name = db.shorten_name(u'companies_company_product_versions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('company', models.ForeignKey(orm[u'companies.company'], null=False)),
            ('productversion', models.ForeignKey(orm[u'companies.productversion'], null=False))
        ))
        db.create_unique(m2m_table_name, ['company_id', 'productversion_id'])


    def backwards(self, orm):
        # Deleting model 'ProductVersion'
        db.delete_table(u'companies_productversion')

        # Deleting model 'Product'
        db.delete_table(u'companies_product')

        # Deleting model 'Company'
        db.delete_table(u'companies_company')

        # Removing M2M table for field product_versions on 'Company'
        db.delete_table(db.shorten_name(u'companies_company_product_versions'))


    models = {
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
        }
    }

    complete_apps = ['companies']