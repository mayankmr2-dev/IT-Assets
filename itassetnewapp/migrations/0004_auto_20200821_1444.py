# Generated by Django 2.1.15 on 2020-08-21 09:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itassetnewapp', '0003_auto_20200821_1442'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='extedenduser',
            new_name='extendeduser',
        ),
    ]