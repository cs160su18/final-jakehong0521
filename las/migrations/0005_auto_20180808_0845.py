# Generated by Django 2.0 on 2018-08-08 08:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('las', '0004_auto_20180807_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='jobDescription',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date(2018, 8, 8)),
        ),
    ]
