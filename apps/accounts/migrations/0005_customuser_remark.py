# Generated by Django 4.0.4 on 2022-06-01 10:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customuser_city_customuser_state_customuser_street'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='remark',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
