# Generated by Django 5.2.3 on 2025-06-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatgroup',
            name='group_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
