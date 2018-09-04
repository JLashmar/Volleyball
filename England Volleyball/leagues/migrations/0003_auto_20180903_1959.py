# Generated by Django 2.1.1 on 2018-09-03 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0004_auto_20180903_1806'),
        ('leagues', '0002_league_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaguetabledata',
            name='team',
        ),
        migrations.AddField(
            model_name='leaguetabledata',
            name='team',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='clubs.Team'),
        ),
    ]