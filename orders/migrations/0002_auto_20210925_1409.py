# Generated by Django 3.2.7 on 2021-09-25 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]