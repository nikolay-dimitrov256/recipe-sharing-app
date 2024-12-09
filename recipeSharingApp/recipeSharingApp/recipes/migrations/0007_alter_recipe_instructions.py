# Generated by Django 5.1.3 on 2024-12-09 11:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_recipe_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(10, message='You can come up with at least 10 characters. Come on, how to cook this?')]),
        ),
    ]
