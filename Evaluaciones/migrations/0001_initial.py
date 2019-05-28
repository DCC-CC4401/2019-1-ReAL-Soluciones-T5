# Generated by Django 2.2.1 on 2019-05-28 03:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Rubricas', '0001_initial'),
        ('Evaluadores', '0001_initial'),
        ('Cursos', '0001_initial'),
        ('Alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo_min', models.PositiveSmallIntegerField(default=5)),
                ('tiempo_max', models.PositiveSmallIntegerField(default=8)),
                ('fecha_inicio', models.DateField(default=django.utils.timezone.now)),
                ('fecha_fin', models.DateField(default=django.utils.timezone.now)),
                ('estado', models.CharField(max_length=7)),
                ('nombre', models.CharField(max_length=100)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cursos.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='FichaEvaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_grupo', models.CharField(max_length=15)),
                ('estado_evaluacion', models.CharField(max_length=15)),
                ('tiempo', models.IntegerField(default=0)),
                ('evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluaciones.Evaluacion')),
                ('evaluador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluadores.Evaluador')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alumnos.Grupo')),
                ('presentador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alumnos.Alumno')),
                ('rubrica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rubricas.AspectoRubrica')),
            ],
        ),
        migrations.CreateModel(
            name='EvaluadoresEvaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluaciones.Evaluacion')),
                ('evaluador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluadores.Evaluador')),
            ],
            options={
                'unique_together': {('evaluacion', 'evaluador')},
            },
        ),
    ]
