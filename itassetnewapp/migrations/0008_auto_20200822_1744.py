# Generated by Django 2.1.15 on 2020-08-22 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itassetnewapp', '0007_auto_20200822_1725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='MAC_address',
            new_name='hostname',
        ),
    ]
