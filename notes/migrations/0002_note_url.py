# Generated by Django 2.0.7 on 2018-07-31 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='url',
            field=models.URLField(blank='True'),
        ),
    ]
