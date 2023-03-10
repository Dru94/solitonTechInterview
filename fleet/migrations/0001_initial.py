# Generated by Django 4.1.6 on 2023-02-10 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=22)),
                ('phone_number', models.IntegerField()),
                ('age', models.IntegerField()),
                ('date_hired', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_number', models.CharField(max_length=200)),
                ('mileage', models.IntegerField()),
                ('manufacturer', models.CharField(max_length=200)),
                ('date_of_purchase', models.DateTimeField(auto_now_add=True)),
                ('drivers', models.ManyToManyField(related_name='cars', to='fleet.driver')),
            ],
        ),
    ]
