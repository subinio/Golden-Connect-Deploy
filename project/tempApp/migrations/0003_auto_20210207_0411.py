# Generated by Django 3.1.6 on 2021-02-06 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempApp', '0002_auto_20210207_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='solution',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
