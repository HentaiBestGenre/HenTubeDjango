# Generated by Django 4.0.4 on 2022-07-10 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Channel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chanel',
            name='date',
        ),
    ]
