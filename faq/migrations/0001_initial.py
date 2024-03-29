# Generated by Django 4.1.5 on 2023-03-04 20:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=32)),
                ('text', models.TextField()),
                ('custom_order', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]
