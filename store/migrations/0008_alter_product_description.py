# Generated by Django 3.2.15 on 2022-08-15 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
