# Generated by Django 3.1.2 on 2020-12-02 18:16

import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import draftjs_sanitizer
import saleor.core.db.fields
import saleor.core.utils.json_serializer


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('private_metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('seo_title', models.CharField(blank=True, max_length=70, null=True, validators=[django.core.validators.MaxLengthValidator(70)])),
                ('seo_description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MaxLengthValidator(300)])),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
                ('content_json', saleor.core.db.fields.SanitizedJSONField(blank=True, default=dict, sanitizer=draftjs_sanitizer.clean_draft_js)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('slug',),
                'permissions': (('manage_pages', 'Manage pages.'),),
            },
        ),
        migrations.CreateModel(
            name='PageTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_title', models.CharField(blank=True, max_length=70, null=True, validators=[django.core.validators.MaxLengthValidator(70)])),
                ('seo_description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MaxLengthValidator(300)])),
                ('language_code', models.CharField(max_length=10)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField(blank=True)),
                ('content_json', saleor.core.db.fields.SanitizedJSONField(blank=True, default=dict, sanitizer=draftjs_sanitizer.clean_draft_js)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='page.page')),
            ],
            options={
                'ordering': ('language_code', 'page', 'pk'),
                'unique_together': {('language_code', 'page')},
            },
        ),
    ]
