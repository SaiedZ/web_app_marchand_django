# Generated by Django 4.0.1 on 2022-01-13 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_remove_band_like_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='biography',
            field=models.TextField(max_length=1000),
        ),
    ]
