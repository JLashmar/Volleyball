# Generated by Django 2.1.1 on 2018-09-10 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0004_auto_20180903_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='club_slug',
            field=models.SlugField(default=2, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]