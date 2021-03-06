# Generated by Django 2.1.5 on 2019-11-08 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0010_auto_20191106_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='profile_shared_list',
            field=models.ManyToManyField(limit_choices_to={'groups_name': 'Docent'}, related_name='accessable_user_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='profile_owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
