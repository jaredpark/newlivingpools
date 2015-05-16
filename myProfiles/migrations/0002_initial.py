# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('myProfiles_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('about_me', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('facebook_id', self.gf('django.db.models.fields.BigIntegerField')(blank=True, unique=True, null=True)),
            ('access_token', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('facebook_name', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
            ('facebook_profile_url', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('website_url', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('blog_url', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(blank=True, max_length=1, null=True)),
            ('raw_data', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('facebook_open_graph', self.gf('django.db.models.fields.NullBooleanField')(blank=True, null=True)),
            ('new_token_required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('image', self.gf('utilities.ContentTypeRestrictedImageField')(blank=True, max_upload_size=2621440, max_length=255, null=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(unique=True, to=orm['auth.User'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(blank=True, default='', max_length=20, null=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(blank=True, default='', max_length=20, null=True)),
            ('address', self.gf('django.db.models.fields.CharField')(blank=True, default='', max_length=60, null=True)),
            ('city', self.gf('django.db.models.fields.CharField')(blank=True, default='', max_length=20, null=True)),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')(blank=True, default='', max_length=5, null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(blank=True, default='', max_length=12, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(blank=True, default='', max_length=40, null=True)),
            ('has_dog', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('locked_gate', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pool_service_customer', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pool_repair_customer', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('home_repair_customer', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('current_balance', self.gf('django.db.models.fields.DecimalField')(blank=True, max_digits=6, default=0.0, null=True, decimal_places=2)),
            ('balance_due_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('scheduled_appointment_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True, default='', max_length=400, null=True)),
        ))
        db.send_create_signal('myProfiles', ['UserProfile'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('myProfiles_userprofile')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Group']", 'related_name': "'user_set'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'myProfiles.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'about_me': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'access_token': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '60', 'null': 'True'}),
            'balance_due_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'blog_url': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '20', 'null': 'True'}),
            'current_balance': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'max_digits': '6', 'default': '0.0', 'null': 'True', 'decimal_places': '2'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'default': "''", 'max_length': '40', 'null': 'True'}),
            'facebook_id': ('django.db.models.fields.BigIntegerField', [], {'blank': 'True', 'unique': 'True', 'null': 'True'}),
            'facebook_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'facebook_open_graph': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'facebook_profile_url': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '20', 'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '1', 'null': 'True'}),
            'has_dog': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'home_repair_customer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('utilities.ContentTypeRestrictedImageField', [], {'blank': 'True', 'max_upload_size': '2621440', 'max_length': '255', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '20', 'null': 'True'}),
            'locked_gate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'new_token_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''", 'max_length': '400', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '12', 'null': 'True'}),
            'pool_repair_customer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pool_service_customer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'raw_data': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'scheduled_appointment_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'unique': 'True', 'to': "orm['auth.User']"}),
            'website_url': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'default': "''", 'max_length': '5', 'null': 'True'})
        }
    }

    complete_apps = ['myProfiles']