# Generated by Django 3.2.3 on 2021-05-31 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0004_alter_youtuber_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtuber',
            name='subs',
            field=models.IntegerField(default='0'),
        ),
    ]
