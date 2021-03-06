# Generated by Django 3.2.3 on 2021-05-26 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('role', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='media/team/%Y/%m/%d')),
                ('fb_link', models.CharField(max_length=250)),
                ('insta_link', models.CharField(max_length=250)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
