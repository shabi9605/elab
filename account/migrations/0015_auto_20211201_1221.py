# Generated by Django 3.2.6 on 2021-12-01 06:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20211201_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='placement',
            name='available_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='placement',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
