# Generated by Django 3.2 on 2021-04-17 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20210416_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='sector',
            field=models.CharField(max_length=50),
        ),
    ]
