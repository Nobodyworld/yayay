# Generated by Django 5.0.4 on 2024-06-23 18:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leveling', '0001_initial'),
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributelevel',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leveling_attributes', to='personas.persona', verbose_name='Persona'),
        ),
        migrations.AddField(
            model_name='skill',
            name='attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='leveling.attribute', verbose_name='Associated Attribute'),
        ),
        migrations.AddField(
            model_name='skilllevel',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persona_skills', to='personas.persona', verbose_name='Persona'),
        ),
        migrations.AddField(
            model_name='skilllevel',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persona_skills', to='leveling.skill', verbose_name='Skill'),
        ),
    ]