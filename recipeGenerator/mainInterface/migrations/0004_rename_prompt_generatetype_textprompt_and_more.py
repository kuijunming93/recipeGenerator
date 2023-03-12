# Generated by Django 4.1.7 on 2023-03-08 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainInterface', '0003_generatetype_prompt_alter_generatetype_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generatetype',
            old_name='prompt',
            new_name='textPrompt',
        ),
        migrations.AddField(
            model_name='generatetype',
            name='imgPrompt',
            field=models.CharField(blank=True, max_length=350),
        ),
    ]