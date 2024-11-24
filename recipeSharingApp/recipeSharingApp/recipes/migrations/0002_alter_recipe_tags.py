# Generated by Django 5.1.3 on 2024-11-23 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_initial'),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='tagged_recipes', to='common.tag'),
        ),
    ]
