# Generated by Django 2.0 on 2018-08-09 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('las', '0007_auto_20180809_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, to='las.Profile'),
        ),
    ]
