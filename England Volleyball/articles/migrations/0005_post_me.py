# Generated by Django 2.1.1 on 2018-09-10 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0004_post_club'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='me',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='test_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
