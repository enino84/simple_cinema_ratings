# Generated by Django 4.0.3 on 2022-04-10 21:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_movie_publicp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release',
            field=models.DateTimeField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
