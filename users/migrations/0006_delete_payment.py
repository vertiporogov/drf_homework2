# Generated by Django 4.2 on 2024-04-07 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_payment_payment_amount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
