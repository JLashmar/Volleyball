# Generated by Django 2.1.1 on 2018-09-03 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_post_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=250)),
            ],
        ),
    ]
