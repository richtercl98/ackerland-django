# Generated by Django 4.1.5 on 2023-03-04 21:42

from django.db import migrations
import faq.models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='topic',
            field=faq.models.LowerCaseCharField(max_length=32),
        ),
    ]
