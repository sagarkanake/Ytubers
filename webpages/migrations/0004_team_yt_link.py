# Generated by Django 3.2.5 on 2021-07-25 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='yt_link',
            field=models.CharField(default='some string', max_length=255),
        ),
    ]
