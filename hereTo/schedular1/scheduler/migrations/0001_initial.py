# Generated by Django 3.1.2 on 2020-11-13 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminComments',
            fields=[
                ('idAdminComments', models.AutoField(primary_key=True, serialize=False)),
                ('Comment', models.CharField(max_length=255)),
                ('creation', models.DateTimeField()),
            ],
            options={
                'db_table': 'admincomments',
                'ordering': ['creation'],
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('idlog', models.AutoField(primary_key=True, serialize=False)),
                ('creation', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('createdBy', models.IntegerField()),
                ('modifiedBy', models.IntegerField()),
                ('tableName', models.CharField(max_length=45)),
                ('modifiedField', models.CharField(max_length=45)),
                ('lastValue', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'logs',
                'ordering': ['creation'],
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('Classroom_idClassroom', models.IntegerField()),
                ('group_idgroup', models.IntegerField()),
                ('Personnel_idPersonnel', models.IntegerField()),
                ('Cours_idCours', models.IntegerField()),
                ('Time_idTime', models.IntegerField()),
                ('Semesters_idSemesters', models.IntegerField()),
                ('idSchedule', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'schedule',
                'ordering': ['Semesters_idSemesters'],
            },
        ),
        migrations.CreateModel(
            name='Semesters',
            fields=[
                ('idSemesters', models.AutoField(primary_key=True, serialize=False)),
                ('semester', models.CharField(max_length=15)),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
            ],
            options={
                'db_table': 'semesters',
                'ordering': ['startTime'],
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('idTime', models.AutoField(primary_key=True, serialize=False)),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
            ],
            options={
                'db_table': 'Times',
                'ordering': ['startTime', 'endTime'],
            },
        ),
    ]