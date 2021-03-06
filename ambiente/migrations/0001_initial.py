# Generated by Django 4.0.6 on 2022-07-14 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('nome_fantasia', models.CharField(max_length=255)),
                ('telefone', models.CharField(blank=True, max_length=255)),
                ('cnpj', models.CharField(blank=True, max_length=255)),
                ('endereco', models.CharField(blank=True, max_length=255)),
                ('cidade', models.CharField(blank=True, max_length=255)),
                ('descricao', models.TextField(blank=True)),
                ('mostrar', models.BooleanField(default=True)),
                ('tipo', models.CharField(choices=[('V', 'Varejo'), ('S', 'Atacado'), ('F', 'Food')], default='V', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=50, null=True)),
                ('processador', models.CharField(blank=True, max_length=50, null=True)),
                ('memoria', models.CharField(blank=True, max_length=50, null=True)),
                ('ip', models.CharField(blank=True, max_length=255, verbose_name='Endereço de IP')),
                ('tipo', models.CharField(choices=[('T', 'Terminal'), ('S', 'Servidor')], default='V', max_length=1)),
                ('ambiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambiente.ambiente')),
            ],
            options={
                'verbose_name': 'Maquina',
                'verbose_name_plural': 'Maquinas',
            },
        ),
    ]
