# Generated by Django 4.0.4 on 2022-05-21 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='ipaddress',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
