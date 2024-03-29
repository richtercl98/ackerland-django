# Generated by Django 4.1.5 on 2023-05-05 15:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('performances', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='act',
            name='corresponding_user',
        ),
        migrations.RemoveField(
            model_name='workshop',
            name='corresponding_user',
        ),
        migrations.AddField(
            model_name='act',
            name='corresponding_users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='workshop',
            name='corresponding_users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
