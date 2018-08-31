# Generated by Django 2.1 on 2018-08-31 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.PositiveSmallIntegerField(choices=[(1, 'player'), (2, 'coach'), (3, 'club secretary'), (4, 'club media'), (5, 'Administrator')], primary_key=True, serialize=False),
        ),
    ]
