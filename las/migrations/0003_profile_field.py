# Generated by Django 2.0 on 2018-08-07 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('las', '0002_auto_20180807_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='field',
            field=models.TextField(choices=[('N/A', 'N/A'), ('Administration', 'administration'), ('Banking', 'banking')], default='N/A'),
        ),
    ]
