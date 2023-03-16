# Generated by Django 4.0.1 on 2023-03-15 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='code',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='discount',
            name='discount',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='discount',
            name='ends_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='discount',
            name='starts_at',
            field=models.DateTimeField(null=True),
        ),
    ]