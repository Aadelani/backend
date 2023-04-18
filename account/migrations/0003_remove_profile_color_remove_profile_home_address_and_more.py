# Generated by Django 4.1.3 on 2022-12-10 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_consumerprofile_profile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='color',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='home_address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='rating',
        ),
        migrations.AlterField(
            model_name='user',
            name='otp',
            field=models.IntegerField(blank=True, default=0, unique=True),
        ),
    ]
