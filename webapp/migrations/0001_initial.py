# Generated by Django 2.1.5 on 2019-11-05 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LKL_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LKL_Dimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LKL_Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('super_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.LKL_Category')),
            ],
        ),
        migrations.CreateModel(
            name='LKL_Subsubcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('super_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.LKL_Subcategory')),
            ],
        ),
        migrations.AddField(
            model_name='lkl_category',
            name='super_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.LKL_Dimension'),
        ),
    ]
