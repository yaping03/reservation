# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-07 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=36)),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Date2Timer',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('confe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Conference')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Date')),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timer', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='date2timer',
            name='people',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.People'),
        ),
        migrations.AddField(
            model_name='date2timer',
            name='timer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Timer'),
        ),
        migrations.AlterUniqueTogether(
            name='date2timer',
            unique_together=set([('timer', 'date')]),
        ),
    ]
