# Generated by Django 4.1.7 on 2023-03-08 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainInterface', '0006_alter_recipe_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
