# Generated by Django 4.0.4 on 2022-05-31 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default=('True', 'True'), max_length=10),
        ),
    ]
