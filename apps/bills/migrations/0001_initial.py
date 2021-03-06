# Generated by Django 2.0 on 2018-01-24 19:29

import apps.bills.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=36, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('debit', models.DecimalField(decimal_places=2, max_digits=8)),
                ('due_date', models.DateField()),
                ('branch', apps.bills.models.CustomForeignKey(db_column='branch_slug', on_delete=django.db.models.deletion.CASCADE, related_name='bills', to='branches.Branch', to_field='slug', verbose_name='branch_slug')),
            ],
            options={
                'verbose_name_plural': 'bills',
                'ordering': ('due_date',),
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=36, unique=True)),
                ('payment_date', models.DateField()),
                ('bill', apps.bills.models.CustomOneToOneField(db_column='bill_slug', on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='bills.Bill', to_field='slug')),
            ],
            options={
                'verbose_name_plural': 'payments',
                'ordering': ('payment_date',),
            },
        ),
    ]
