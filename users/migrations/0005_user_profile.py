# Generated by Django 3.0.7 on 2020-07-05 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200705_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
