# Generated by Django 3.1.6 on 2021-02-07 10:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movieslist', '0002_auto_20210207_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='contributors',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
