# Generated by Django 3.2.9 on 2021-11-28 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0010_auto_20211026_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='season_year',
            field=models.TextField(default='Fall 2021'),
        ),
    ]
