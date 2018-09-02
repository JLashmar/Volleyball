# Generated by Django 2.1 on 2018-09-01 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20180901_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='name',
            field=models.CharField(default='none', max_length=255),
        ),
        migrations.AlterField(
            model_name='position',
            name='name',
            field=models.CharField(default='none', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Role'),
        ),
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
