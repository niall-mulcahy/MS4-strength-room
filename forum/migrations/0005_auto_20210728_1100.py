# Generated by Django 3.2.5 on 2021-07-28 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_category_friendly_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
