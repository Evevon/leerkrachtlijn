# Generated by Django 2.1.5 on 2019-11-19 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_auto_20191118_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='lkl_resource',
            name='upva_resource',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lkl_resource',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
