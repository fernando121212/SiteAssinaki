
# Generated by Django 2.1.3 on 2018-11-26 19:55

# Generated by Django 2.1.3 on 2018-11-26 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Bairro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bairro_nome', models.CharField(max_length=50, verbose_name='Nome do bairro')),
            ],
            options={
                'verbose_name': 'Bairro',
                'verbose_name_plural': 'Bairro',
            },
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade_nome', models.CharField(max_length=50, verbose_name='Nome da cidade')),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
            },
=======
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade_nome', models.CharField(max_length=50)),
            ],
>>>>>>> origin/master
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('pais_nome', models.CharField(max_length=50, verbose_name='Nome do país')),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Países',
            },
=======
                ('pais_nome', models.CharField(max_length=50)),
            ],
>>>>>>> origin/master
        ),
        migrations.CreateModel(
            name='Uf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('uf_nome', models.CharField(max_length=50, verbose_name='Nome do  estado')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='assinaki.Pais')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
=======
                ('uf_nome', models.CharField(max_length=50)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='assinaki.Pais')),
            ],
>>>>>>> origin/master
        ),
        migrations.AddField(
            model_name='cidade',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='assinaki.Uf'),
        ),
<<<<<<< HEAD
        migrations.AddField(
            model_name='bairro',
            name='cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='assinaki.Cidade'),
        ),
=======
>>>>>>> origin/master
    ]
