# Generated by Django 3.0.3 on 2020-02-14 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0008_auto_20200219_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammembers',
            name='user',
            field=models.ForeignKey(db_column='user_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]