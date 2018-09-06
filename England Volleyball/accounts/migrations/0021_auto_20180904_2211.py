# Generated by Django 2.1.1 on 2018-09-04 21:11

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20180902_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='position',
        ),
        migrations.AddField(
            model_name='profile',
            name='position',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='continent', chained_model_field='role', default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Position'),
        ),
    ]
