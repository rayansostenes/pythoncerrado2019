# Generated by Django 2.2.5 on 2019-09-05 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sorteio', '0005_auto_20190905_1043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='perfil_instagram',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='qr_code',
        ),
    ]
