# Generated by Django 3.1.2 on 2020-12-02 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(allow_unicode=True, max_length=255, unique=True)),
            ],
            options={
                'ordering': ('pk',),
                'permissions': (('manage_menus', 'Manage navigation.'),),
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(db_index=True, editable=False, null=True)),
                ('name', models.CharField(max_length=128)),
                ('url', models.URLField(blank=True, max_length=256, null=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'ordering': ('sort_order', 'pk'),
            },
        ),
        migrations.CreateModel(
            name='MenuItemTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=128)),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='menu.menuitem')),
            ],
            options={
                'ordering': ('language_code', 'menu_item', 'pk'),
            },
        ),
    ]
