# Generated by Django 3.0.8 on 2020-07-12 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20200711_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
