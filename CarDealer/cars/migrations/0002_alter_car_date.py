# Generated by Django 3.2.7 on 2021-09-04 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='date',
            field=models.DateField(),
        ),
    ]
