# Generated by Django 4.1.2 on 2022-12-05 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_product_price_price_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Price',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]