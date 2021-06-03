# Generated by Django 3.2.1 on 2021-06-03 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_salesregioncategorymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesCountryMonthModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(max_length=50)),
                ('Month', models.CharField(max_length=50)),
                ('NetAmount', models.IntegerField()),
                ('Tax', models.IntegerField()),
                ('TotalAmount', models.IntegerField()),
            ],
        ),
    ]