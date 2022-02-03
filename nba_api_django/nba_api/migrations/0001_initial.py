# Generated by Django 3.2.12 on 2022-02-03 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conference', models.CharField(choices=[('E', 'Eastern'), ('W', 'Western')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('wins', models.IntegerField(max_length=10)),
                ('losses', models.IntegerField(max_length=10)),
                ('conf_championships', models.IntegerField(max_length=10)),
                ('nba_championships', models.IntegerField(max_length=10)),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='nba_api.conference')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('age', models.IntegerField(max_length=3)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='nba_api.team')),
            ],
        ),
    ]
