# Generated by Django 3.0.4 on 2020-06-20 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0028_auto_20200514_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='answer',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='task',
            name='question',
            field=models.CharField(max_length=500),
        ),
    ]