# Generated by Django 5.0.4 on 2024-04-13 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_requestgetoptimalroutechat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vetka',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='vershina',
            name='description',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Des',
        ),
    ]