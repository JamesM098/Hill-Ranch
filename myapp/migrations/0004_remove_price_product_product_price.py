# Generated by Django 4.1.2 on 2022-12-05 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_product_alter_cow_cow_parent_alter_cow_cow_notes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
