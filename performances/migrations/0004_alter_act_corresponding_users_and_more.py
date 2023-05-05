# Generated by Django 4.1.5 on 2023-05-05 09:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('performances', '0003_remove_act_sound_sample_url_act_insta_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act',
            name='corresponding_users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='corresponding_users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
