# Generated by Django 3.2.4 on 2021-10-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_auto_20211012_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header_Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PageName', models.CharField(max_length=32)),
                ('CSVheader', models.CharField(max_length=32)),
                ('DBheader', models.CharField(max_length=32)),
                ('created_date', models.DateTimeField()),
                ('modified_date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='semester',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
