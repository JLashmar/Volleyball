# Generated by Django 2.1 on 2018-08-31 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180901_0005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='gender',
            new_name='Position',
        ),
    ]