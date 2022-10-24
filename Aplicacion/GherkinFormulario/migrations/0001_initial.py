# Generated by Django 4.1.2 on 2022-10-23 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CasoPrueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPNombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CPAtributo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPAtributo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LenguajeGherkin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SentenciaNombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PseudoAlgoritmoCasoPrueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPPaso', models.CharField(max_length=255)),
                ('CPResultado', models.CharField(max_length=255)),
                ('LenguajeGherkinFK', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GherkinFormulario.lenguajegherkin')),
            ],
        ),
        migrations.CreateModel(
            name='AtributosCasoPrueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPValorAtributo', models.CharField(max_length=255)),
                ('CPAtributoFK', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GherkinFormulario.cpatributo')),
                ('CasoPruebaFK', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GherkinFormulario.casoprueba')),
            ],
        ),
    ]
