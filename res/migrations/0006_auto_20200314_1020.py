# Generated by Django 3.0.2 on 2020-03-14 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0005_remove_event_places_trip_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_places',
            name='user_id',
        ),
        migrations.AddField(
            model_name='event_places',
            name='vendor_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='res.vendor'),
        ),
    ]
