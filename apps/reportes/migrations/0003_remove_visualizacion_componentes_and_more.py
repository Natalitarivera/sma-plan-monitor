# Generated by Django 5.1.7 on 2025-04-13 15:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('medidas', '0002_componente_alter_logmedida_options_and_more'),
        ('organismos', '0003_tipoorganismo_alter_organismo_options_and_more'),
        ('reportes', '0002_reportegenerado_activo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visualizacion',
            name='componentes',
        ),
        migrations.RemoveField(
            model_name='visualizacion',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='visualizacion',
            name='organismos',
        ),
        migrations.AlterModelOptions(
            name='reportegenerado',
            options={'ordering': ['-fecha_generacion'], 'verbose_name': 'Reporte Generado', 'verbose_name_plural': 'Reportes Generados'},
        ),
        migrations.AlterModelOptions(
            name='tiporeporte',
            options={'verbose_name': 'Tipo de Reporte', 'verbose_name_plural': 'Tipos de Reportes'},
        ),
        migrations.RemoveField(
            model_name='reportegenerado',
            name='activo',
        ),
        migrations.RemoveField(
            model_name='reportegenerado',
            name='componentes',
        ),
        migrations.RemoveField(
            model_name='reportegenerado',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='reportegenerado',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='reportegenerado',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='reportegenerado',
            name='fecha_solicitud',
        ),
        migrations.RemoveField(
            model_name='reportegenerado',
            name='mensaje_error',
        ),
        migrations.RemoveField(
            model_name='reportegenerado',
            name='organismos',
        ),
        migrations.RemoveField(
            model_name='reportegenerado',
            name='publico',
        ),
        migrations.RemoveField(
            model_name='reportegenerado',
            name='solicitado_por',
        ),
        migrations.RemoveField(
            model_name='reportegenerado',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='tiporeporte',
            name='activo',
        ),
        migrations.RemoveField(
            model_name='tiporeporte',
            name='icono',
        ),
        migrations.RemoveField(
            model_name='tiporeporte',
            name='publico',
        ),
        migrations.RemoveField(
            model_name='tiporeporte',
            name='slug',
        ),
        migrations.AddField(
            model_name='reportegenerado',
            name='componente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reportes', to='medidas.componente', verbose_name='Componente'),
        ),
        migrations.AddField(
            model_name='reportegenerado',
            name='organismo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reportes', to='organismos.organismo', verbose_name='Organismo'),
        ),
        migrations.AddField(
            model_name='reportegenerado',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reportes_generados', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tiporeporte',
            name='acceso_admin_sma',
            field=models.BooleanField(default=True, verbose_name='Acceso Admin SMA'),
        ),
        migrations.AddField(
            model_name='tiporeporte',
            name='acceso_organismos',
            field=models.BooleanField(default=False, verbose_name='Acceso Organismos'),
        ),
        migrations.AddField(
            model_name='tiporeporte',
            name='acceso_superadmin',
            field=models.BooleanField(default=True, verbose_name='Acceso Superadmin'),
        ),
        migrations.AddField(
            model_name='tiporeporte',
            name='tipo',
            field=models.CharField(choices=[('general', 'Reporte General'), ('organismo', 'Reporte por Organismo'), ('componente', 'Reporte por Componente')], default=1, max_length=20, verbose_name='Tipo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reportegenerado',
            name='archivo',
            field=models.FileField(upload_to='reportes/%Y/%m/', verbose_name='Archivo'),
        ),
        migrations.AlterField(
            model_name='reportegenerado',
            name='fecha_generacion',
            field=models.DateTimeField(default=timezone.now, verbose_name='Fecha de generación'),
        ),
        migrations.AlterField(
            model_name='reportegenerado',
            name='parametros',
            field=models.JSONField(blank=True, default=dict, verbose_name='Parámetros'),
        ),
        migrations.AlterField(
            model_name='reportegenerado',
            name='tipo_reporte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reportes_generados', to='reportes.tiporeporte', verbose_name='Tipo de reporte'),
        ),
        migrations.DeleteModel(
            name='ParametroReporte',
        ),
        migrations.DeleteModel(
            name='Visualizacion',
        ),
    ]
