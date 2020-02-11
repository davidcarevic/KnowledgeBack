# Generated by Django 3.0.3 on 2020-02-11 10:45

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_emailinvitation'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailinvitation',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='emailinvitation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
