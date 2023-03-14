# Generated by Django 4.1.7 on 2023-03-14 06:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainInterface', '0011_alter_recipe_imgpath'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipeType',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 14, 6, 31, 40, 528979, tzinfo=datetime.timezone.utc)),
        ),
    ]