# Generated by Django 2.1 on 2018-09-01 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20180901_0020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='position',
        ),
        migrations.AddField(
            model_name='position',
            name='name',
            field=models.CharField(default='None', max_length=255),
        ),
    ]