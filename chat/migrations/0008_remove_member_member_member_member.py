# Generated by Django 5.2.3 on 2025-07-09 07:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_alter_chatgroup_group_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='member',
        ),
        migrations.AddField(
            model_name='member',
            name='member',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='joined_groups', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
