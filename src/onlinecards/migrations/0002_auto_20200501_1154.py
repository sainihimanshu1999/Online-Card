# Generated by Django 3.0.2 on 2020-05-01 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdash',
            name='id',
        ),
        migrations.AddField(
            model_name='userdash',
            name='user_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]