# Generated by Django 5.0.4 on 2024-06-23 18:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leveling', '0002_initial'),
        ('metrics', '0001_initial'),
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personametrics',
            name='persona',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='metrics', to='personas.persona'),
        ),
        migrations.AddField(
            model_name='rating',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='personas.persona'),
        ),
        migrations.AddField(
            model_name='rating',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='leveling.skill'),
        ),
    ]
