# Generated by Django 3.0.2 on 2020-03-29 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0009_vehicles_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='res.Roles'),
        ),
    ]