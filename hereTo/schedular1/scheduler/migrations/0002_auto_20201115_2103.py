# Generated by Django 3.1.2 on 2020-11-16 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AdminComments',
            new_name='AdminComment',
        ),
        migrations.RenameModel(
            old_name='Logs',
            new_name='Log',
        ),
        migrations.RenameModel(
            old_name='Semesters',
            new_name='Semester',
        ),
    ]