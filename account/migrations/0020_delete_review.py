# Generated by Django 3.2.6 on 2021-12-01 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_alter_review_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]