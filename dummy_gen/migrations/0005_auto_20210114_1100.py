# Generated by Django 3.1.5 on 2021-01-14 09:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummy_gen', '0004_auto_20210114_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheme',
            name='c2',
            field=models.CharField(choices=[('1', 'Choose...'), ('2', 'Name'), ('3', 'Job'), ('4', 'Company'), ('5', 'Date'), ('6', 'E-mail')], default='Choose...', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='c3',
            field=models.CharField(choices=[('1', 'Choose...'), ('2', 'Name'), ('3', 'Job'), ('4', 'Company'), ('5', 'Date'), ('6', 'E-mail')], default='Choose...', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='c4',
            field=models.CharField(choices=[('1', 'Choose...'), ('2', 'Name'), ('3', 'Job'), ('4', 'Company'), ('5', 'Date'), ('6', 'E-mail')], default='Choose...', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='c5',
            field=models.CharField(choices=[('1', 'Choose...'), ('2', 'Name'), ('3', 'Job'), ('4', 'Company'), ('5', 'Date'), ('6', 'E-mail')], default='Choose...', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='n1',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='n2',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='n3',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='n4',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='n5',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='o1',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='scheme',
            name='o2',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='scheme',
            name='o3',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='scheme',
            name='o4',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='scheme',
            name='o5',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='scheme',
            name='rows',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
