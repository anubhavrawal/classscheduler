# Generated by Django 3.2.4 on 2021-09-19 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='crn',
            field=models.IntegerField(unique=True),
        ),
    ]
