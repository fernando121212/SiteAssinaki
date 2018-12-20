# Generated by Django 2.1.3 on 2018-12-20 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assinatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=11, verbose_name='Assinatura')),
                ('slug', models.SlugField(max_length=150, verbose_name='Identificador')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Cliente', verbose_name='Cliente')),
                ('preco_base', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.PrecoAssinatura', verbose_name='Preço base')),
            ],
            options={
                'verbose_name': 'Assinatura',
                'verbose_name_plural': 'Assinaturas',
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Documento')),
                ('slug', models.SlugField(max_length=150, verbose_name='Identificador')),
                ('documento_data', models.DateField(verbose_name='Disponível até')),
                ('documento_quantidade_partes', models.IntegerField(verbose_name='Quantas partes')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('tipo_documento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Tipo_documento', verbose_name='Tipo de documento')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
        ),
        migrations.CreateModel(
            name='DocumentoAssinado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Documento assinado')),
                ('slug', models.SlugField(max_length=15, verbose_name='Identificador')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Cliente', verbose_name='Cliente')),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='services.Documento', verbose_name='Documento')),
            ],
            options={
                'verbose_name': 'Documento assinado',
                'verbose_name_plural': 'Documentos assinados',
            },
        ),
    ]
