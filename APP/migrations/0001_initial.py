# Generated by Django 3.2.11 on 2024-04-23 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=55)),
                ('Email', models.EmailField(max_length=55)),
                ('Number', models.IntegerField(max_length=15)),
                ('Date', models.DateField()),
                ('Persons', models.IntegerField(max_length=2)),
            ],
        ),
    ]
