# Generated by Django 2.1.1 on 2018-09-10 13:07

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20180910_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='club',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='me', chained_model_field='name', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='club', to='clubs.Club'),
        ),
    ]