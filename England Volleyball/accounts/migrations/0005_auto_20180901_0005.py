# Generated by Django 2.1 on 2018-08-31 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180831_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='name',
        ),
        migrations.AddField(
            model_name='position',
            name='gender',
            field=models.CharField(choices=[('Coach', 'Coach'), ('Press Officer', 'Press Officer'), ('Referees', 'Referees')], default='Coach', max_length=50),
        ),
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Player'), (2, 'Administrator'), (3, 'Offical')], primary_key=True, serialize=False),
        ),
    ]
