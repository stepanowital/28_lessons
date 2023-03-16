# Generated by Django 4.0.1 on 2023-03-15 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='attractions',
            field=models.ManyToManyField(to='edits.Attractions'),
        ),
        migrations.AddField(
            model_name='tour',
            name='children_ok',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='end_point',
            field=models.CharField(default=True, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='group_size',
            field=models.SmallIntegerField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='guide',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='edits.guide'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='language',
            field=models.CharField(choices=[('ru', 'Русский'), ('en', 'Английский'), ('jp', 'Японский')], default='ru', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='price_rur',
            field=models.DecimalField(decimal_places=2, default=True, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='start_point',
            field=models.CharField(default=True, max_length=20),
            preserve_default=False,
        ),
    ]
