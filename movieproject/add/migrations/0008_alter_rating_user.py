# Generated by Django 5.0.4 on 2024-04-28 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add', '0007_alter_rating_movie_alter_rating_out_of_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]
