# Generated by Django 3.0.2 on 2020-04-01 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0014_auto_20200402_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='no_of_rooms',
            field=models.IntegerField(default=0),
        ),
    ]
