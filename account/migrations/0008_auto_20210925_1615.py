# Generated by Django 3.2.7 on 2021-09-25 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_register_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='register',
            name='status',
        ),
    ]