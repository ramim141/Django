# Generated by Django 5.0.4 on 2024-05-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
