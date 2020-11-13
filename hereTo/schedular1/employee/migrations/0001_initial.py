# Generated by Django 3.1.2 on 2020-11-13 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('idAvailability', models.AutoField(primary_key=True, serialize=False)),
                ('day', models.CharField(max_length=45)),
                ('statTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('note', models.CharField(max_length=45)),
                ('notavailable', models.BinaryField()),
                ('status', models.BinaryField()),
                ('Personnel_idPersonnel', models.IntegerField()),
            ],
            options={
                'db_table': 'availabilities',
                'ordering': ['statTime'],
            },
        ),
        migrations.CreateModel(
            name='Personnels',
            fields=[
                ('idPersonnel', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=45)),
                ('lastName', models.CharField(max_length=45)),
                ('personalEmail', models.CharField(max_length=45)),
                ('hiredate', models.DateField()),
                ('emailMatrix', models.CharField(max_length=45)),
                ('position', models.CharField(max_length=45)),
                ('profession', models.CharField(max_length=45)),
                ('note', models.CharField(max_length=45)),
                ('status', models.BinaryField()),
                ('code', models.IntegerField()),
            ],
            options={
                'db_table': 'personnels',
                'ordering': ['hiredate'],
            },
        ),
        migrations.CreateModel(
            name='TeacherPreferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Personnels_idPersonnel', models.IntegerField()),
                ('Cours_idCours', models.IntegerField()),
                ('Note', models.CharField(max_length=150)),
                ('rank', models.BinaryField()),
            ],
            options={
                'db_table': 'teacherpreferences',
            },
        ),
    ]
