# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 22:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PinResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_type', models.CharField(choices=[('WA', 'Wrong Answer'), ('AC', 'Accepted'), ('XE', 'Execution Error'), ('CE', 'Compilation Error'), ('TLE', 'Time Limit Exceeded')], max_length=3)),
                ('time', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PinTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cin', models.TextField(blank=True, null=True)),
                ('cout', models.TextField(blank=True, null=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_type', models.CharField(choices=[('WA', 'Wrong Answer'), ('AC', 'Accepted'), ('XE', 'Execution Error'), ('CE', 'Compilation Error'), ('TLE', 'Time Limit Exceeded')], max_length=3)),
                ('time', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(blank=True, null=True)),
                ('compiled', models.BooleanField(default=False)),
                ('compilator_output', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('enabled', models.BooleanField(default=True)),
                ('custom_comparator_enabled', models.BooleanField(default=False)),
                ('custom_comparator', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cin', models.TextField(blank=True, null=True)),
                ('cout', models.TextField(blank=True, null=True)),
                ('enabled', models.BooleanField(default=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='bugfreefiesta.Task')),
            ],
        ),
        migrations.AddField(
            model_name='submission',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='bugfreefiesta.Task'),
        ),
        migrations.AddField(
            model_name='result',
            name='submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='bugfreefiesta.Submission'),
        ),
        migrations.AddField(
            model_name='result',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='bugfreefiesta.Test'),
        ),
        migrations.AddField(
            model_name='pintest',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pin_tests', to='bugfreefiesta.Task'),
        ),
        migrations.AddField(
            model_name='pinresult',
            name='pin_test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='bugfreefiesta.PinTest'),
        ),
        migrations.AddField(
            model_name='pinresult',
            name='submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pin_results', to='bugfreefiesta.Submission'),
        ),
    ]
