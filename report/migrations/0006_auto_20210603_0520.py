# Generated by Django 3.2.1 on 2021-06-03 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_salescountrymonthmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salescountrymonthmodel',
            name='NetAmount',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='salescountrymonthmodel',
            name='Tax',
            field=models.IntegerField(blank=True),
        ),
    ]