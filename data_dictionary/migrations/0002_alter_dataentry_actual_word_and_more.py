# Generated by Django 5.0.4 on 2024-04-22 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_dictionary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataentry',
            name='actual_word',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='dataentry',
            name='replaced_word',
            field=models.CharField(max_length=1000),
        ),
    ]