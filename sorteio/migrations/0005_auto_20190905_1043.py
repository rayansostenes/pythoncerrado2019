# Generated by Django 2.2.5 on 2019-09-05 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorteio', '0004_sorteio_aberto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorteio',
            name='inscritos',
            field=models.ManyToManyField(blank=True, null=True, to='sorteio.Pessoa'),
        ),
    ]
