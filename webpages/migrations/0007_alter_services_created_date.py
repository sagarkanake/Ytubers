# Generated by Django 3.2.5 on 2021-07-31 03:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0006_alter_services_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
