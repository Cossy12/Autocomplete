# Generated by Django 4.0.5 on 2022-06-28 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autosearch', '0002_rename_address_searchoption_searched'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searchoption',
            old_name='searched',
            new_name='address',
        ),
    ]
