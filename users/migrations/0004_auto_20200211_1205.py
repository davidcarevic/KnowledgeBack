# Generated by Django 3.0.3 on 2020-02-11 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200211_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailinvitation',
            name='token',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
