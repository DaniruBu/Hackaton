# Generated by Django 5.0.4 on 2024-04-13 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_messagegpt_delete_countmessages'),
    ]

    operations = [
        migrations.CreateModel(
            name='HobbyGPT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]