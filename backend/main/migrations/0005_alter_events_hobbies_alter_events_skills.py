# Generated by Django 5.0.4 on 2024-04-12 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_events_description_alter_events_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='hobbies',
            field=models.ManyToManyField(blank=True, to='main.hobby'),
        ),
        migrations.AlterField(
            model_name='events',
            name='skills',
            field=models.ManyToManyField(blank=True, to='main.skill'),
        ),
    ]
