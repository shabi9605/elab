# Generated by Django 3.2.7 on 2021-10-03 04:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_blogmodel_commentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
