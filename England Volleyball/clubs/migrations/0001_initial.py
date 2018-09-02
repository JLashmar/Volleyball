# Generated by Django 2.1 on 2018-08-31 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=100)),
                ('post_code', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Mixed', 'Mixed')], default='Men', max_length=5)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clubs.Club')),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
    ]