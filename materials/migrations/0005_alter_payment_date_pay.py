# Generated by Django 4.2 on 2024-04-07 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0004_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='date_pay',
            field=models.DateField(blank=True, null=True, verbose_name='дата платежа'),
        ),
    ]
