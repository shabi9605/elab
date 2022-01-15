# Generated by Django 3.2.7 on 2021-09-28 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teacher', '0007_auto_20210928_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessons',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]