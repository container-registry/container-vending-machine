# Generated by Django 3.1.4 on 2020-12-16 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sync', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='expiry_date',
        ),
    ]