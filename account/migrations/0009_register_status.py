# Generated by Django 3.2.7 on 2021-09-25 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20210925_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
