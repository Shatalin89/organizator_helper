# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 05:00
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(blank=True, max_length=30)),
                ('date_birthday', models.DateField(blank=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('vk_id', models.URLField(blank=True)),
                ('fb_id', models.URLField(blank=True)),
                ('insta_id', models.URLField(blank=True)),
            ],
        ),
    ]