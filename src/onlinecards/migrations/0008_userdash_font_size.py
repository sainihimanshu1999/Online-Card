# Generated by Django 3.0.2 on 2020-04-28 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecards', '0007_auto_20200428_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdash',
            name='font_size',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]