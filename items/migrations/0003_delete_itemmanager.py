# Generated by Django 4.0.1 on 2022-02-07 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_item'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ItemManager',
        ),
    ]
