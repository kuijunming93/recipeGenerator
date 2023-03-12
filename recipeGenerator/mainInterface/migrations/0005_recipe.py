# Generated by Django 4.1.7 on 2023-03-08 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainInterface', '0004_rename_prompt_generatetype_textprompt_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('imgPath', models.URLField(blank=True)),
                ('content', models.CharField(blank=True, max_length=1000)),
            ],
        ),
    ]