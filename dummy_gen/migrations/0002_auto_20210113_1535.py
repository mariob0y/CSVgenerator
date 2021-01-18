# Generated by Django 3.1.5 on 2021-01-13 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummy_gen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='John', max_length=30)),
                ('last_name', models.CharField(default='Smith', max_length=30)),
                ('job', models.CharField(default='Plumber', max_length=30)),
                ('company', models.CharField(default='Nintendo', max_length=30)),
                ('date', models.DateField(auto_now_add=True)),
                ('email', models.EmailField(default='adress@email.com', max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='scheme',
            name='phone',
            field=models.IntegerField(blank=True, default=0, max_length=12),
        ),
    ]
