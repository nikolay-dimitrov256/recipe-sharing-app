# Generated by Django 5.1.3 on 2024-12-05 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at']},
        ),
    ]
