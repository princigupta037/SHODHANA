# Generated by Django 2.1.7 on 2020-02-16 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200215_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default=True, max_length=100)),
                ('password', models.CharField(default=True, max_length=100)),
            ],
        ),
    ]
