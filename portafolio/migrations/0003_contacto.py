# Generated by Django 4.2.5 on 2023-09-10 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0002_alter_portafolio_github_alter_portafolio_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
            ],
        ),
    ]
