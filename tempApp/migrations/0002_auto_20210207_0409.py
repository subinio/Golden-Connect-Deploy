# Generated by Django 3.1.6 on 2021-02-06 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='solution',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]