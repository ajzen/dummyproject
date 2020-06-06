# Generated by Django 3.0.5 on 2020-06-06 09:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('locker', '0011_rankinglist_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='availability',
            name='timings_closed',
            field=models.TimeField(default='22:00'),
        ),
        migrations.AlterField(
            model_name='availability',
            name='timings_open',
            field=models.TimeField(default='07:00'),
        ),
        migrations.AlterField(
            model_name='occupancy',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='occupancy',
            name='occupancy',
            field=models.FloatField(default=2),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=2.5, max_digits=2),
        ),
        migrations.AlterField(
            model_name='throughput',
            name='throughput',
            field=models.FloatField(default=5.6),
        ),
    ]
