# Generated by Django 4.2.5 on 2023-11-28 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0005_auto_20220609_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
