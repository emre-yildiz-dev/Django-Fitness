# Generated by Django 4.0.4 on 2022-06-02 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customuser_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='images/avatar.jpeg', null=True, upload_to='images/'),
        ),
    ]
