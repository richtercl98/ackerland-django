# Generated by Django 4.1.5 on 2023-05-04 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performances', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act',
            name='sound_sample_url',
            field=models.URLField(blank=True),
        ),
    ]