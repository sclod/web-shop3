# Generated by Django 3.1.7 on 2021-03-12 23:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210312_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 12, 23, 46, 7, 511986)),
        ),
    ]
