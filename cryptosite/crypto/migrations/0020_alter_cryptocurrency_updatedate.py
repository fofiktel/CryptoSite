# Generated by Django 4.1.2 on 2022-10-18 19:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0019_alter_cryptocurrency_updatedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency',
            name='UpdateDate',
            field=models.DateField(default=datetime.datetime(2022, 10, 18, 19, 35, 42, 193287, tzinfo=datetime.timezone.utc)),
        ),
    ]
