# Generated by Django 3.2.7 on 2021-09-28 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_course_user'),
        ('teacher', '0008_lessons_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.course'),
        ),
    ]
