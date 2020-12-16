# Generated by Django 3.1.2 on 2020-12-02 18:16

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import oauthlib.common
import saleor.core.utils.json_serializer


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('name', models.CharField(max_length=60)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('type', models.CharField(choices=[('local', 'local'), ('thirdparty', 'thirdparty')], default='local', max_length=60)),
                ('identifier', models.CharField(blank=True, max_length=256, null=True)),
                ('about_app', models.TextField(blank=True, null=True)),
                ('data_privacy', models.TextField(blank=True, null=True)),
                ('data_privacy_url', models.URLField(blank=True, null=True)),
                ('homepage_url', models.URLField(blank=True, null=True)),
                ('support_url', models.URLField(blank=True, null=True)),
                ('configuration_url', models.URLField(blank=True, null=True)),
                ('app_url', models.URLField(blank=True, null=True)),
                ('version', models.CharField(blank=True, max_length=60, null=True)),
                ('permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this app.', related_name='app_set', related_query_name='app', to='auth.Permission')),
            ],
            options={
                'ordering': ('name', 'pk'),
                'permissions': (('manage_apps', 'Manage apps'),),
            },
        ),
        migrations.CreateModel(
            name='AppToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=128)),
                ('auth_token', models.CharField(default=oauthlib.common.generate_token, max_length=30, unique=True)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tokens', to='app.app')),
            ],
        ),
        migrations.CreateModel(
            name='AppInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('success', 'Success'), ('failed', 'Failed'), ('deleted', 'Deleted')], default='pending', max_length=50)),
                ('message', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('app_name', models.CharField(max_length=60)),
                ('manifest_url', models.URLField()),
                ('permissions', models.ManyToManyField(blank=True, help_text='Specific permissions which will be assigned to app.', related_name='app_installation_set', related_query_name='app_installation', to='auth.Permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
