# Generated by Django 4.0.4 on 2022-06-01 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_service_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name=range(0, 6)),
        ),
    ]
