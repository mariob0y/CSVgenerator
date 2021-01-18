# Generated by Django 3.1.5 on 2021-01-14 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dummy_gen', '0007_article_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheme',
            name='user',
        ),
        migrations.AddField(
            model_name='scheme',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
