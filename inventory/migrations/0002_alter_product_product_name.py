# Generated by Django 4.0.1 on 2022-01-25 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
