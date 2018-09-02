# Generated by Django 2.1 on 2018-09-01 11:32

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20180901_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='role', chained_model_field='role', on_delete=django.db.models.deletion.CASCADE, to='accounts.Position'),
        ),
    ]
