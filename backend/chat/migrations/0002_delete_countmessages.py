# Generated by Django 5.0.4 on 2024-04-13 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CountMessages',
        ),
    ]