# Generated by Django 2.2.3 on 2019-07-22 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('body', models.TextField()),
                ('number', models.CharField(max_length=15)),
                ('isbn', models.CharField(max_length=10)),
            ],
        ),
    ]
