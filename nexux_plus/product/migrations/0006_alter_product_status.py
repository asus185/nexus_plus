# Generated by Django 5.1.5 on 2025-03-28 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_status_alter_productimage_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Active'), ('Inactive', 2), (3, 'Sold')], default=1),
        ),
    ]
