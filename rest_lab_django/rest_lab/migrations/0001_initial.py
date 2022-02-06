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
                ('conference', models.TextField(max_length=100)),
                ('num_wins', models.CharField(max_length=50)),
                ('num_losses', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no player name', max_length=100)),
                ('posistion', models.CharField(default='no posistion', max_length=100)),
                ('age', models.CharField(max_length=200, null=True)),
                ('is_injured', models.CharField(max_length=200, null=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='rest.team')),
            ],
        ),
    ]