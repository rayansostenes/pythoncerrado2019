# Generated by Django 2.2.5 on 2019-09-05 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorteio', '0006_auto_20190905_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='old',
            field=models.BooleanField(default=False),
        ),
    ]
