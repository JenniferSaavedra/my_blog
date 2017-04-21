# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 22:03
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_logentry_remove_auto_add'),
        ('auth', '0008_alter_user_username_max_length'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('carrera_id', models.AutoField(primary_key=True, serialize=False)),
                ('carrera_codigo', models.CharField(max_length=10)),
                ('carrera_descripcion', models.CharField(choices=[('P', 'Maestria Profundización'), ('I', 'Maestria Investigación'), ('D', 'Doctorado')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('estado_id', models.AutoField(primary_key=True, serialize=False)),
                ('estado_descripcion', models.CharField(choices=[('SO', 'Por_Someter'), ('AV', 'Por_Avalar'), ('EV', 'Por_Evaluar'), ('SU', 'Por_Sustentar'), ('FI', 'Finalizado'), ('AN', 'Anulado')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('persona_id', models.AutoField(primary_key=True, serialize=False)),
                ('persona_escolaridad', models.CharField(choices=[('M', 'Maestria'), ('D', 'Doctorado')], max_length=1, null=True)),
                ('persona_carrera', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Carrera')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Propuesta',
            fields=[
                ('propuesta_id', models.AutoField(primary_key=True, serialize=False)),
                ('propuesta_tipo', models.CharField(choices=[('P', 'Maestria Profundización'), ('I', 'Maestria Investigación'), ('D', 'Doctorado')], max_length=1)),
                ('propuesta_titulo', models.CharField(max_length=70)),
                ('codirector_propuesta', models.CharField(max_length=50)),
                ('propuesta_estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Estado')),
                ('propuesta_estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('registro_id', models.AutoField(primary_key=True, serialize=False)),
                ('registro_fecha', models.DateTimeField(auto_now=True)),
                ('registro_aula', models.CharField(max_length=30, null=True)),
                ('registro_observaciones', models.CharField(max_length=200, null=True)),
                ('registro_hora_sustentacion', models.TimeField(null=True)),
                ('registro_fecha_sustentacion', models.DateField(null=True)),
                ('registro_estado_actual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Estado')),
                ('registro_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Persona')),
                ('registro_propuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Propuesta')),
            ],
        ),
        migrations.CreateModel(
            name='Rol_usuario',
            fields=[
                ('rol_id', models.AutoField(primary_key=True, serialize=False)),
                ('rol_tipo', models.CharField(choices=[('ES', 'Estudiante'), ('TU', 'Tutor'), ('CO', 'Coordinador'), ('EV', 'Evaluador'), ('SE', 'Secretaria')], default=1, max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='coordinador',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='evaluador',
            name='filiacion_evaluador',
        ),
        migrations.RemoveField(
            model_name='evaluador',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='secretaria',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='filiacion_tutor',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='user_ptr',
        ),
        migrations.RenameField(
            model_name='filiacion',
            old_name='departamento_filiacion',
            new_name='filiacion_departamento',
        ),
        migrations.RenameField(
            model_name='filiacion',
            old_name='grupo_filiacion',
            new_name='filiacion_grupo',
        ),
        migrations.RenameField(
            model_name='filiacion',
            old_name='id_filiacion',
            new_name='filiacion_id',
        ),
        migrations.RenameField(
            model_name='filiacion',
            old_name='universidad_filiacion',
            new_name='filiacion_universidad',
        ),
        migrations.DeleteModel(
            name='Coordinador',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Evaluador',
        ),
        migrations.DeleteModel(
            name='secretaria',
        ),
        migrations.DeleteModel(
            name='Tutor',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='persona',
            name='persona_filiacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Filiacion'),
        ),
    ]
