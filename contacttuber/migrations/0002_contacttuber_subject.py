# Generated by Django 3.2.5 on 2021-07-31 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacttuber', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacttuber',
            name='subject',
            field=models.CharField(default='some', max_length=250),
        ),
    ]