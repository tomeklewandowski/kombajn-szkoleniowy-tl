# Generated by Django 2.1.3 on 2018-11-25 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_exercise_exercisestudent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercisestudent',
            options={'verbose_name': 'Zadanie zrobione przez studenta', 'verbose_name_plural': 'Zadania zrobione przez studentów'},
        ),
    ]
