# Generated by Django 2.1.7 on 2020-02-11 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='your_number',
            field=models.CharField(default='Your number', max_length=10),
        ),
    ]
