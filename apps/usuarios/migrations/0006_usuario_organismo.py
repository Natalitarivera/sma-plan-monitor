# Generated by Django 5.1.7 on 2025-04-02 01:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organismos', '0002_organismo_created_at_organismo_updated_at'),
        ('usuarios', '0005_remove_usuario_organismo'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='organismo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='organismos.organismo'),
            preserve_default=False,
        ),
    ]
