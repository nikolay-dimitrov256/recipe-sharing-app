# Generated by Django 5.1.3 on 2024-12-09 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipe_created_at_alter_recipe_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
