# Generated by Django 3.0.7 on 2020-07-05 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile',
        ),
    ]