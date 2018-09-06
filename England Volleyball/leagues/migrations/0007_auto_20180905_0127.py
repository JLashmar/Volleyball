# Generated by Django 2.1.1 on 2018-09-05 00:27

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0006_auto_20180905_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaguetabledata',
            name='team',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='league', chained_model_field='team', on_delete=django.db.models.deletion.CASCADE, related_name='table_team', to='clubs.Team'),
        ),
    ]
