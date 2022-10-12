# Generated by Django 4.1.2 on 2022-10-11 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0006_cryptocurrency_circulatingsupply_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptocurrency',
            name='ChangePrice',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cryptocurrency',
            name='UpdateDate',
            field=models.DateField(default=datetime.datetime(2022, 10, 11, 18, 35, 52, 190353, tzinfo=datetime.timezone.utc)),
        ),
    ]