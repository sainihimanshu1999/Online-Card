# Generated by Django 3.0.2 on 2020-04-29 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecards', '0010_auto_20200428_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdash',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]