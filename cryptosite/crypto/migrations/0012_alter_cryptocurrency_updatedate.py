# Generated by Django 4.1.2 on 2022-10-18 09:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0011_alter_cryptocurrency_updatedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency',
            name='UpdateDate',
            field=models.DateField(default=datetime.datetime(2022, 10, 18, 9, 7, 53, 352336, tzinfo=datetime.timezone.utc)),
        ),
    ]
