# Generated by Django 3.1.2 on 2020-10-19 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20201019_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventinstance',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_instances', to='events.place'),
        ),
    ]
