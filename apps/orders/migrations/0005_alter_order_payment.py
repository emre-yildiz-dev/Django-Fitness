# Generated by Django 4.0.4 on 2022-05-31 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_price_alter_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(blank=True, choices=[('Cash', 'Cash'), ('Credit Card', 'Credit Card')], max_length=255, null=True),
        ),
    ]
