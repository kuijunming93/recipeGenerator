# Generated by Django 4.1.7 on 2023-03-14 06:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainInterface', '0012_recipe_recipetype_recipe_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 14, 6, 41, 7, 329226, tzinfo=datetime.timezone.utc)),
        ),
    ]
