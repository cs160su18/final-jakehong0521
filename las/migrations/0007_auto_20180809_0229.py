# Generated by Django 2.0 on 2018-08-09 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('las', '0006_auto_20180809_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, default=[], related_name='_profile_followers_+', to='las.Profile'),
        ),
    ]
