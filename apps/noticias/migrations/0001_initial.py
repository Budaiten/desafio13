# Generated by Django 4.2.3 on 2023-07-21 22:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('subtitulo', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('texto', models.TextField()),
                ('activo', models.BooleanField(default=True)),
                ('imagen', models.ImageField(blank=True, default='static/noticia_default.png', null=True, upload_to='media')),
                ('publicado', models.DateTimeField(default=django.utils.timezone.now)),
                ('categoria', models.ForeignKey(default='Sin Categoria', null=True, on_delete=django.db.models.deletion.SET_NULL, to='noticias.categoria')),
            ],
            options={
                'ordering': ('-publicado',),
            },
        ),
    ]
