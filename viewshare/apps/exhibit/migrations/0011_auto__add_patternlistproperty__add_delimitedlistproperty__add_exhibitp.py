# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PatternListProperty'
        db.create_table('exhibit_patternlistproperty', (
            ('exhibitproperty_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['exhibit.ExhibitProperty'], unique=True, primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['exhibit.ExhibitProperty'])),
            ('pattern', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('exhibit', ['PatternListProperty'])

        # Adding model 'DelimitedListProperty'
        db.create_table('exhibit_delimitedlistproperty', (
            ('exhibitproperty_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['exhibit.ExhibitProperty'], unique=True, primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['exhibit.ExhibitProperty'])),
            ('delimiter', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('exhibit', ['DelimitedListProperty'])

        # Adding model 'ExhibitProperty'
        db.create_table('exhibit_exhibitproperty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classname', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
            ('exhibit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='properties', to=orm['exhibit.Exhibit'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value_type', self.gf('django.db.models.fields.CharField')(default='text', max_length=10)),
        ))
        db.send_create_signal('exhibit', ['ExhibitProperty'])

        # Adding unique constraint on 'ExhibitProperty', fields ['exhibit', 'name']
        db.create_unique('exhibit_exhibitproperty', ['exhibit_id', 'name'])

        # Adding model 'PropertyReference'
        db.create_table('exhibit_propertyreference', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('derived', self.gf('django.db.models.fields.related.ForeignKey')(related_name='properties', to=orm['exhibit.CompositeProperty'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exhibit.ExhibitProperty'])),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('exhibit', ['PropertyReference'])

        # Adding unique constraint on 'PropertyReference', fields ['derived', 'source']
        db.create_unique('exhibit_propertyreference', ['derived_id', 'source_id'])

        # Adding model 'CompositeProperty'
        db.create_table('exhibit_compositeproperty', (
            ('exhibitproperty_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['exhibit.ExhibitProperty'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('exhibit', ['CompositeProperty'])

        # Adding model 'DataJSONFile'
        db.create_table('exhibit_datajsonfile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exhibit', self.gf('django.db.models.fields.related.OneToOneField')(related_name='data', unique=True, to=orm['exhibit.Exhibit'])),
            ('json', self.gf('django.db.models.fields.TextField')(default='{}')),
        ))
        db.send_create_signal('exhibit', ['DataJSONFile'])


    def backwards(self, orm):
        # Removing unique constraint on 'PropertyReference', fields ['derived', 'source']
        db.delete_unique('exhibit_propertyreference', ['derived_id', 'source_id'])

        # Removing unique constraint on 'ExhibitProperty', fields ['exhibit', 'name']
        db.delete_unique('exhibit_exhibitproperty', ['exhibit_id', 'name'])

        # Deleting model 'PatternListProperty'
        db.delete_table('exhibit_patternlistproperty')

        # Deleting model 'DelimitedListProperty'
        db.delete_table('exhibit_delimitedlistproperty')

        # Deleting model 'ExhibitProperty'
        db.delete_table('exhibit_exhibitproperty')

        # Deleting model 'PropertyReference'
        db.delete_table('exhibit_propertyreference')

        # Deleting model 'CompositeProperty'
        db.delete_table('exhibit_compositeproperty')

        # Deleting model 'DataJSONFile'
        db.delete_table('exhibit_datajsonfile')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'dataset.dataset': {
            'Meta': {'ordering': "('-modified',)", 'unique_together': "(('slug', 'owner'),)", 'object_name': 'Dataset'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'datasets'", 'null': 'True', 'to': "orm['auth.User']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'title'", 'overwrite': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'exhibit.canvas': {
            'Meta': {'object_name': 'Canvas'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'title'", 'overwrite': 'False'}),
            'thumbnail': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'exhibit.compositeproperty': {
            'Meta': {'object_name': 'CompositeProperty', '_ormbases': ['exhibit.ExhibitProperty']},
            'exhibitproperty_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exhibit.ExhibitProperty']", 'unique': 'True', 'primary_key': 'True'})
        },
        'exhibit.datajsonfile': {
            'Meta': {'object_name': 'DataJSONFile'},
            'exhibit': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'data'", 'unique': 'True', 'to': "orm['exhibit.Exhibit']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('django.db.models.fields.TextField', [], {'default': "'{}'"})
        },
        'exhibit.delimitedlistproperty': {
            'Meta': {'object_name': 'DelimitedListProperty', '_ormbases': ['exhibit.ExhibitProperty']},
            'delimiter': ('django.db.models.fields.TextField', [], {}),
            'exhibitproperty_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exhibit.ExhibitProperty']", 'unique': 'True', 'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['exhibit.ExhibitProperty']"})
        },
        'exhibit.draftexhibit': {
            'Meta': {'ordering': "('-modified',)", 'object_name': 'DraftExhibit', '_ormbases': ['exhibit.Exhibit']},
            'exhibit_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exhibit.Exhibit']", 'unique': 'True', 'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'draft_exhibits'", 'null': 'True', 'to': "orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['exhibit.PublishedExhibit']", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        'exhibit.exhibit': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Exhibit'},
            'canvas': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['exhibit.Canvas']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dataset': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'exhibits'", 'null': 'True', 'to': "orm['dataset.Dataset']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'profile': ('django.db.models.fields.TextField', [], {'default': "'{}'"})
        },
        'exhibit.exhibitproperty': {
            'Meta': {'unique_together': "(('exhibit', 'name'),)", 'object_name': 'ExhibitProperty'},
            'classname': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'exhibit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'properties'", 'to': "orm['exhibit.Exhibit']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value_type': ('django.db.models.fields.CharField', [], {'default': "'text'", 'max_length': '10'})
        },
        'exhibit.patternlistproperty': {
            'Meta': {'object_name': 'PatternListProperty', '_ormbases': ['exhibit.ExhibitProperty']},
            'exhibitproperty_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exhibit.ExhibitProperty']", 'unique': 'True', 'primary_key': 'True'}),
            'pattern': ('django.db.models.fields.TextField', [], {}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['exhibit.ExhibitProperty']"})
        },
        'exhibit.propertyreference': {
            'Meta': {'ordering': "('order',)", 'unique_together': "(('derived', 'source'),)", 'object_name': 'PropertyReference'},
            'derived': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'properties'", 'to': "orm['exhibit.CompositeProperty']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['exhibit.ExhibitProperty']"})
        },
        'exhibit.publishedexhibit': {
            'Meta': {'ordering': "('-modified',)", 'unique_together': "(('slug', 'owner'),)", 'object_name': 'PublishedExhibit', '_ormbases': ['exhibit.Exhibit']},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'exhibit_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exhibit.Exhibit']", 'unique': 'True', 'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'published_exhibits'", 'null': 'True', 'to': "orm['auth.User']"}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'title'", 'overwrite': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['exhibit']