# Generated by Django 2.1.1 on 2018-09-04 22:19

from django.db import migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_profile_team'),
        ('fixtures', '0012_auto_20180904_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchdata',
            name='b_squad',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_field='team_b', chained_model_field='team', horizontal=True, related_name='b_squad', to='accounts.Profile', verbose_name='b_squad'),
        ),
        migrations.AlterField(
            model_name='matchdata',
            name='a_squad',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_field='team_a', chained_model_field='team', horizontal=True, related_name='a_squad', to='accounts.Profile', verbose_name='a_squad'),
        ),
    ]
