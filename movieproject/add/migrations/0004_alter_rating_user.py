# Generated by Django 5.0.4 on 2024-04-27 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add', '0003_alter_rating_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.IntegerField(),
        ),
    ]
