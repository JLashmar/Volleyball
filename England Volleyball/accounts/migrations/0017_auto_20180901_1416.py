# Generated by Django 2.1 on 2018-09-01 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20180901_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publication',
        ),
        migrations.RemoveField(
            model_name='book',
            name='writer',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='publications',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
        migrations.DeleteModel(
            name='Writer',
        ),
    ]
