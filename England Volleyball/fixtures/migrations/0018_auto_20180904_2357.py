# Generated by Django 2.1.1 on 2018-09-04 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0017_auto_20180904_2356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matchdata',
            old_name='b_squad',
            new_name='team_a_squad',
        ),
        migrations.RemoveField(
            model_name='matchdata',
            name='a_squad',
        ),
    ]
