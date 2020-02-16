# Generated by Django 2.1.7 on 2020-02-11 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200211_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='your_email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='your_name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='your_number',
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default='name', max_length=50),
        ),
        migrations.AddField(
            model_name='contact',
            name='phonenumber',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='your_mail',
            field=models.CharField(default='mail', max_length=50),
        ),
        migrations.AlterModelTable(
            name='contact',
            table='contact',
        ),
    ]
