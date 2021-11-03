# Generated by Django 2.0.1 on 2018-01-04 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ago', models.IntegerField(verbose_name='Ano')),
                ('description', models.CharField(max_length=500, verbose_name='Descrição')),
                ('image', models.ImageField(upload_to='home/quemsomos', verbose_name='Imagem')),
                ('time', models.DateTimeField(verbose_name='Hora')),
                ('time2', models.DateTimeField(verbose_name='Hora2')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Quem Somos',
                'verbose_name': 'Quem Somos',
                'ordering': ['ago'],
            },
        ),
    ]