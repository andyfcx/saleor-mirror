# Generated by Django 3.1.2 on 2020-12-02 18:16

import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import saleor.checkout.models
import saleor.core.utils.json_serializer
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('private_metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_change', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254)),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('note', models.TextField(blank=True, default='')),
                ('currency', models.CharField(default='TWD', max_length=3)),
                ('country', django_countries.fields.CountryField(default=saleor.checkout.models.get_default_country, max_length=2)),
                ('discount_amount', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('discount_name', models.CharField(blank=True, max_length=255, null=True)),
                ('translated_discount_name', models.CharField(blank=True, max_length=255, null=True)),
                ('voucher_code', models.CharField(blank=True, max_length=12, null=True)),
                ('redirect_url', models.URLField(blank=True, null=True)),
                ('tracking_code', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ('-last_change', 'pk'),
                'permissions': (('manage_checkouts', 'Manage checkouts'),),
            },
        ),
        migrations.CreateModel(
            name='CheckoutLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='checkout.checkout')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
