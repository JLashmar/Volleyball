# Generated by Django 2.1.1 on 2018-09-10 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0004_auto_20180903_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='club_slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
