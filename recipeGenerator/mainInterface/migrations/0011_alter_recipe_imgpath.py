# Generated by Django 4.1.7 on 2023-03-14 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainInterface', '0010_recipe_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='imgPath',
            field=models.URLField(blank=True, max_length=1000),
        ),
    ]