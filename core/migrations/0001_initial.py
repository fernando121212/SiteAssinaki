# Generated by Django 2.1.3 on 2018-12-20 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrecoAssinatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço base')),
                ('slug', models.SlugField(max_length=150, verbose_name='Identificador')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Preço base',
                'verbose_name_plural': 'Preços bases',
            },
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Título')),
                ('slug', models.SlugField(max_length=150, verbose_name='Identificador')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('texto', models.TextField(verbose_name='Conteúdo')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Imagem')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Atualização',
                'verbose_name_plural': 'Atualizações',
            },
        ),
        migrations.CreateModel(
            name='StatusPagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('cartao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Dados_cartao', verbose_name='4 últimos dígitos do cartão')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Cliente', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Status do pagamento',
                'verbose_name_plural': 'Status dos pagamentos',
            },
        ),
        migrations.CreateModel(
            name='Tipo_documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Tipo de documento')),
                ('slug', models.SlugField(max_length=150, verbose_name='Identificador')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Tipo de documento',
                'verbose_name_plural': 'Tipos de documentos',
            },
        ),
    ]
