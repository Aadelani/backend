# Generated by Django 4.1.3 on 2022-12-08 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConsumerProfile',
            new_name='Profile',
        ),
        migrations.RenameField(
            model_name='tempuser',
            old_name='phoneNumber',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
        migrations.DeleteModel(
            name='TechnicianProfile',
        ),
    ]