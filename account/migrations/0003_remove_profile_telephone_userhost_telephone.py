# Generated by Django 4.2.2 on 2023-06-23 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_profile_is_host_remove_profile_passport_photo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='telephone',
        ),
        migrations.AddField(
            model_name='userhost',
            name='telephone',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]