# Generated by Django 3.0.2 on 2020-04-28 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='normal',
        ),
        migrations.RemoveField(
            model_name='room',
            name='pent_house',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_category',
        ),
    ]
