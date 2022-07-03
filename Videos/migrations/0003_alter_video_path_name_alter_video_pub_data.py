# Generated by Django 4.0.4 on 2022-07-02 11:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Videos', '0002_alter_video_pub_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='path_name',
            field=models.FileField(upload_to='Videos/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='pub_data',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 2, 11, 30, 9, 920167, tzinfo=utc), verbose_name='date published'),
        ),
    ]
