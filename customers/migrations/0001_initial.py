# Generated by Django 5.1.5 on 2025-02-25 18:04

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='img')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='UZ')),
                ('address', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('vat_number', models.PositiveIntegerField(blank=True, null=True)),
                ('invoice_prefix', models.CharField(blank=True, max_length=35, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
