# Generated by Django 5.0 on 2025-04-03 21:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMeasure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_of_measure', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockReason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_at', models.DateTimeField(auto_now_add=True)),
                ('finish_at', models.DateTimeField(blank=True, null=True)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bar_code', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('description', models.TextField()),
                ('is_bulk', models.BooleanField(default=False)),
                ('start_at', models.DateTimeField(auto_now_add=True)),
                ('finish_at', models.DateTimeField(blank=True, null=True)),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stores.store')),
                ('unit_of_measure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.productmeasure')),
            ],
        ),
        migrations.CreateModel(
            name='productCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/')),
                ('is_primary', models.BooleanField(default=False)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPriceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price_without_iva', models.DecimalField(decimal_places=2, max_digits=12)),
                ('unit_price_with_iva', models.DecimalField(decimal_places=2, max_digits=12)),
                ('start_at', models.DateTimeField(auto_now_add=True)),
                ('finish_at', models.DateTimeField(blank=True, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductStockHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('start_at', models.DateTimeField(auto_now_add=True)),
                ('finish_at', models.DateTimeField(blank=True, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
                ('reason', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.stockreason')),
            ],
        ),
    ]
