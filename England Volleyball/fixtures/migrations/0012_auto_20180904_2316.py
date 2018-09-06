# Generated by Django 2.1.1 on 2018-09-04 22:16

from django.db import migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0011_auto_20180904_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchdata',
            name='a_squad',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_field='team_a', chained_model_field='team', horizontal=True, to='accounts.Profile', verbose_name='a_squad'),
        ),
    ]
