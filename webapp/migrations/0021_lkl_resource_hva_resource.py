# Generated by Django 2.1.5 on 2019-11-29 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0020_auto_20191125_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='lkl_resource',
            name='hva_resource',
            field=models.BooleanField(default=False),
        ),
    ]
