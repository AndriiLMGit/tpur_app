# Generated by Django 4.2.2 on 2023-06-23 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_host',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='passport_photo',
        ),
        migrations.CreateModel(
            name='UserHost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_host', models.BooleanField(default=False)),
                ('passport_photos', models.FileField(blank=True, null=True, upload_to='user/passports/')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hosts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Host',
            },
        ),
    ]
