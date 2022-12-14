# Generated by Django 4.1.2 on 2022-10-28 19:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_cryptoassets_buy_information_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoldInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold_date', models.DateField(default=django.utils.timezone.now)),
                ('amount_sold_crypto', models.FloatField(default=0)),
                ('sold_price', models.FloatField(default=0)),
                ('CryptoAssets', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.cryptoassets')),
            ],
        ),
    ]
