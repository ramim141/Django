# Generated by Django 5.0.4 on 2024-05-11 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='author',
            name='phone_no',
            field=models.CharField(default='123456789', max_length=12),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
