# Generated by Django 3.0.4 on 2020-03-26 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telnet_server', '0003_versions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Versions',
            new_name='Version',
        ),
    ]