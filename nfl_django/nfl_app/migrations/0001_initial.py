# Generated by Django 4.0.2 on 2022-02-02 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('conference', models.CharField(max_length=100)),
                ('wins', models.IntegerField()),
                ('losses', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('injured_reserved_list', models.BooleanField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nfl_app.team')),
            ],
        ),
    ]
