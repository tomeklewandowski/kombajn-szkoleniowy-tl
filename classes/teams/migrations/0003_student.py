# Generated by Django 2.1.3 on 2018-11-25 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Imię')),
                ('surname', models.CharField(max_length=60, verbose_name='Nazwisko')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('github_nick', models.CharField(max_length=100, verbose_name='Nick na githubie')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Group', verbose_name='Grupa')),
            ],
            options={
                'verbose_name': 'Kursant',
                'verbose_name_plural': 'Kursanci',
            },
        ),
    ]
