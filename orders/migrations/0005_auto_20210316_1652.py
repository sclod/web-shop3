# Generated by Django 3.1.7 on 2021-03-16 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20210312_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 16, 52, 36, 444775)),
        ),
    ]