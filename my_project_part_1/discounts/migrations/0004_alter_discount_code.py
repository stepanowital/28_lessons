# Generated by Django 4.0.1 on 2023-03-15 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0003_discount_tour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='code',
            field=models.CharField(max_length=50, null=True),
        ),
    ]