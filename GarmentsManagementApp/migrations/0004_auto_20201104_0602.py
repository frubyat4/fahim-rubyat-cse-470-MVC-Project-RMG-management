# Generated by Django 3.1.2 on 2020-11-04 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GarmentsManagementApp', '0003_remove_garment_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='TotalPrice',
            field=models.BigIntegerField(),
        ),
    ]
