# Generated by Django 3.2.4 on 2021-12-02 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0014_auto_20211202_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='link1',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='semester',
            name='link2',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
