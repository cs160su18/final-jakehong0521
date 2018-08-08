# Generated by Django 2.0 on 2018-08-07 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('las', '0003_profile_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='aboutMe',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='field',
            field=models.TextField(choices=[('N/A', 'N/A'), ('administration', 'Administration'), ('banking', 'Banking'), ('design', 'Design'), ('education', 'Education'), ('engineering', 'Engineering'), ('entrepreneur', 'Entrepreneur'), ('government', 'Government'), ('health', 'Health'), ('legal', 'Legal'), ('media', 'Media'), ('research', 'Research'), ('sales', 'Sales')], default='N/A'),
        ),
    ]