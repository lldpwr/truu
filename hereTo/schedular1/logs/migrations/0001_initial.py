# Generated by Django 3.1.2 on 2020-11-13 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('createdBy', models.IntegerField()),
                ('modifiedBy', models.IntegerField()),
                ('tableName', models.CharField(max_length=15)),
                ('modifiedField', models.CharField(max_length=15)),
                ('lastValue', models.TextField(max_length=255)),
            ],
        ),
    ]
