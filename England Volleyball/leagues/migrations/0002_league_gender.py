# Generated by Django 2.1.1 on 2018-09-03 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='gender',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Mixed', 'Mixed')], default='Men', max_length=5),
        ),
    ]
