# Generated by Django 2.2.5 on 2019-09-05 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorteio', '0003_auto_20190905_0609'),
    ]

    operations = [
        migrations.AddField(
            model_name='sorteio',
            name='aberto',
            field=models.BooleanField(default=False),
        ),
    ]
