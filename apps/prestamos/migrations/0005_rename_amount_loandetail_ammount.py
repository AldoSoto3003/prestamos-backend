# Generated by Django 4.2.3 on 2024-01-03 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0004_loan_loandetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loandetail',
            old_name='amount',
            new_name='ammount',
        ),
    ]
