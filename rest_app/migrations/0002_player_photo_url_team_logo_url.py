# Generated by Django 4.0.2 on 2022-02-03 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='photo_url',
            field=models.TextField(default='no photo'),
        ),
        migrations.AddField(
            model_name='team',
            name='logo_url',
            field=models.TextField(default='no logo'),
        ),
    ]
