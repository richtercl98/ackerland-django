# Generated by Django 4.1.5 on 2023-03-20 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_alter_faq_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='topic',
            field=models.CharField(max_length=32),
        ),
    ]
