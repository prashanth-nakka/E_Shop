# Generated by Django 3.2.15 on 2022-08-15 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
