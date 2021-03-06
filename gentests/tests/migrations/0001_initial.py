# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-11-26 23:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tag', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=30)),
                ('answer', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to='')),
                ('tip', models.CharField(max_length=30)),
                ('tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tests.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_of_test', models.CharField(max_length=30)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tests.Task')),
            ],
        ),
    ]
