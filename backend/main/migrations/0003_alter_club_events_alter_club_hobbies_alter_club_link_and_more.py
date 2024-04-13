# Generated by Django 5.0.4 on 2024-04-12 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_user_age_alter_user_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='events',
            field=models.ManyToManyField(blank=True, to='main.events'),
        ),
        migrations.AlterField(
            model_name='club',
            name='hobbies',
            field=models.ManyToManyField(blank=True, to='main.hobby'),
        ),
        migrations.AlterField(
            model_name='club',
            name='link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='club',
            name='schedule',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='club',
            name='skills',
            field=models.ManyToManyField(blank=True, to='main.skill'),
        ),
        migrations.AlterField(
            model_name='events',
            name='social_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='hobby',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='hobby',
            name='skills',
            field=models.ManyToManyField(blank=True, to='main.skill'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
