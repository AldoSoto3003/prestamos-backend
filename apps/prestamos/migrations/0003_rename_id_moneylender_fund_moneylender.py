# Generated by Django 4.2.3 on 2023-11-11 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0002_rename_fondo_fund_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fund',
            old_name='id_moneylender',
            new_name='moneylender',
        ),
    ]
