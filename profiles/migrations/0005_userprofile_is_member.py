# Generated by Django 3.2.5 on 2021-08-17 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_userprofile_paid_until'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_member',
            field=models.BooleanField(default=False),
        ),
    ]