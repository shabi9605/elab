# Generated by Django 3.2.7 on 2021-09-25 04:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_register_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.course'),
            preserve_default=False,
        ),
    ]
