# Generated by Django 3.0.5 on 2020-04-29 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lockers', '0011_auto_20200429_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='lockerid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='lockers.Onboard'),
        ),
    ]
