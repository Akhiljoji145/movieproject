# Generated by Django 5.0.4 on 2024-04-27 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add', '0002_rating_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.CharField(max_length=250),
        ),
    ]