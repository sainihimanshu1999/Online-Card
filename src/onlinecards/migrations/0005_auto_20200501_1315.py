# Generated by Django 3.0.2 on 2020-05-01 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecards', '0004_auto_20200501_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdash',
            name='user_id',
        ),
        migrations.AddField(
            model_name='userdash',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
