# Generated by Django 3.0.3 on 2020-02-19 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_auto_20200212_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammembers',
            name='team',
            field=models.ForeignKey(db_column='team_id', on_delete=django.db.models.deletion.CASCADE, to='main.Teams'),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='user',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teamprojects',
            name='project',
            field=models.ForeignKey(db_column='project_id', on_delete=django.db.models.deletion.CASCADE, to='main.Projects'),
        ),
        migrations.AlterField(
            model_name='teamprojects',
            name='team',
            field=models.ForeignKey(db_column='team_id', on_delete=django.db.models.deletion.CASCADE, to='main.Teams'),
        ),
    ]