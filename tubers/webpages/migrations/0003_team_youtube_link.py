# Generated by Django 3.2.3 on 2021-05-28 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='youtube_link',
            field=models.CharField(default='', max_length=250),
        ),
    ]