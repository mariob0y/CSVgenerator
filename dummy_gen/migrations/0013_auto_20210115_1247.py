# Generated by Django 3.1.5 on 2021-01-15 10:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummy_gen', '0012_auto_20210115_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheme',
            name='c1',
            field=models.CharField(choices=[('0', 'Choose...'), ('1', 'name'), ('2', 'job'), ('3', 'company'), ('4', 'date'), ('5', 'email')], default='Choose...', max_length=30),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='c2',
            field=models.CharField(choices=[('0', 'Choose...'), ('1', 'name'), ('2', 'job'), ('3', 'company'), ('4', 'date'), ('5', 'email')], default='Choose...', max_length=30),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='c3',
            field=models.CharField(choices=[('0', 'Choose...'), ('1', 'name'), ('2', 'job'), ('3', 'company'), ('4', 'date'), ('5', 'email')], default='Choose...', max_length=30),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='c4',
            field=models.CharField(choices=[('0', 'Choose...'), ('1', 'name'), ('2', 'job'), ('3', 'company'), ('4', 'date'), ('5', 'email')], default='Choose...', max_length=30),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='c5',
            field=models.CharField(choices=[('0', 'Choose...'), ('1', 'name'), ('2', 'job'), ('3', 'company'), ('4', 'date'), ('5', 'email')], default='Choose...', max_length=30),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='o1',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='o2',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='o3',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='o4',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='o5',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
