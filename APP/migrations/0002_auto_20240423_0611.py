# Generated by Django 3.2.11 on 2024-04-23 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_table',
            name='Number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book_table',
            name='Persons',
            field=models.IntegerField(),
        ),
    ]