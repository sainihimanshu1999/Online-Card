# Generated by Django 3.0.2 on 2020-04-27 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecards', '0002_auto_20200427_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdash',
            name='aboutme',
            field=models.TextField(max_length=1000),
        ),
    ]
