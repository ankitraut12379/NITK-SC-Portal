# Generated by Django 2.2.2 on 2019-06-20 11:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20190620_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='time_of_announcement',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 6, 20, 16, 37, 23, 975042)),
        ),
    ]
