# Generated by Django 2.1.1 on 2018-09-02 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20180902_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.ManyToManyField(to='accounts.Position'),
        ),
    ]
