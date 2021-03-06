# Generated by Django 2.1.15 on 2020-08-22 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itassetnewapp', '0004_auto_20200821_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP_address', models.CharField(max_length=50)),
                ('MAC_address', models.CharField(max_length=50)),
                ('business_name', models.CharField(max_length=50)),
                ('hosting_location', models.CharField(max_length=50)),
                ('db_make_model', models.CharField(max_length=50)),
                ('primary_role', models.CharField(max_length=50)),
                ('mobile_no', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=50)),
                ('billingcount', models.CharField(max_length=30)),
                ('source', models.CharField(max_length=40)),
                ('severity', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Asset',
                'verbose_name_plural': 'Assets',
                'db_table': 'asset_table',
            },
        ),
    ]
