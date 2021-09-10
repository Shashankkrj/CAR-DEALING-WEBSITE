# Generated by Django 3.0.7 on 2020-06-18 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='categories',
        ),
        migrations.AddField(
            model_name='listing',
            name='categories',
            field=models.ManyToManyField(to='listings.Category'),
        ),
    ]
