# Generated by Django 3.1.5 on 2021-01-16 09:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummy_gen', '0015_scheme_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheme',
            name='c6',
            field=models.CharField(choices=[('1', 'Choose...'), ('2', 'name'), ('3', 'job'), ('4', 'company'), ('5', 'date'), ('6', 'phone'), ('7', 'address'), ('8', 'city'), ('9', 'country'), ('10', 'email')], default='Choose...', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='c7',
            field=models.CharField(choices=[('1', 'Choose...'), ('2', 'name'), ('3', 'job'), ('4', 'company'), ('5', 'date'), ('6', 'phone'), ('7', 'address'), ('8', 'city'), ('9', 'country'), ('10', 'email')], default='Choose...', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='c8',
            field=models.CharField(choices=[('1', 'Choose...'), ('2', 'name'), ('3', 'job'), ('4', 'company'), ('5', 'date'), ('6', 'phone'), ('7', 'address'), ('8', 'city'), ('9', 'country'), ('10', 'email')], default='Choose...', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='c9',
            field=models.CharField(choices=[('1', 'Choose...'), ('2', 'name'), ('3', 'job'), ('4', 'company'), ('5', 'date'), ('6', 'phone'), ('7', 'address'), ('8', 'city'), ('9', 'country'), ('10', 'email')], default='Choose...', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='n6',
            field=models.CharField(blank=True, default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='n7',
            field=models.CharField(blank=True, default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='n8',
            field=models.CharField(blank=True, default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='n9',
            field=models.CharField(blank=True, default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='o6',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)]),
        ),
        migrations.AddField(
            model_name='scheme',
            name='o7',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)]),
        ),
        migrations.AddField(
            model_name='scheme',
            name='o8',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)]),
        ),
        migrations.AddField(
            model_name='scheme',
            name='o9',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)]),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='c1',
            field=models.CharField(choices=[('1', 'Choose...'), ('2', 'name'), ('3', 'job'), ('4', 'company'), ('5', 'date'), ('6', 'phone'), ('7', 'address'), ('8', 'city'), ('9', 'country'), ('10', 'email')], default='Choose...', max_length=30),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='c2',
            field=models.CharField(choices=[('1', 'Choose...'), ('2', 'name'), ('3', 'job'), ('4', 'company'), ('5', 'date'), ('6', 'phone'), ('7', 'address'), ('8', 'city'), ('9', 'country'), ('10', 'email')], default='Choose...', max_length=30),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='c3',
            field=models.CharField(choices=[('1', 'Choose...'), ('2', 'name'), ('3', 'job'), ('4', 'company'), ('5', 'date'), ('6', 'phone'), ('7', 'address'), ('8', 'city'), ('9', 'country'), ('10', 'email')], default='Choose...', max_length=30),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='c4',
            field=models.CharField(choices=[('1', 'Choose...'), ('2', 'name'), ('3', 'job'), ('4', 'company'), ('5', 'date'), ('6', 'phone'), ('7', 'address'), ('8', 'city'), ('9', 'country'), ('10', 'email')], default='Choose...', max_length=30),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='c5',
            field=models.CharField(choices=[('1', 'Choose...'), ('2', 'name'), ('3', 'job'), ('4', 'company'), ('5', 'date'), ('6', 'phone'), ('7', 'address'), ('8', 'city'), ('9', 'country'), ('10', 'email')], default='Choose...', max_length=30),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='o1',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)]),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='o2',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)]),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='o3',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)]),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='o4',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)]),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='o5',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)]),
        ),
    ]
