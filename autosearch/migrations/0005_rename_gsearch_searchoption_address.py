# Generated by Django 4.0.5 on 2022-06-28 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autosearch', '0004_rename_address_searchoption_gsearch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searchoption',
            old_name='gsearch',
            new_name='address',
        ),
    ]
