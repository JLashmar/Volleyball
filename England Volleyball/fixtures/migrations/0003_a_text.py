# Generated by Django 2.1.1 on 2018-09-04 15:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0002_auto_20180904_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='a',
            name='text',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
