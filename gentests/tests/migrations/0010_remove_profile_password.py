# Generated by Django 2.2.7 on 2019-12-17 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0009_auto_20191217_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
    ]
