# Generated by Django 3.1.4 on 2020-12-23 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20201223_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.IntegerField(choices=[(1, 'male'), (2, 'female'), (0, 'Null'), (3, 'Not provided')], default=0),
        ),
    ]