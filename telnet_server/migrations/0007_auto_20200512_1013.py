# Generated by Django 3.0.5 on 2020-05-12 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telnet_server', '0006_auto_20200327_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='content_left_panel',
            field=models.TextField(default=10000, max_length=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='template',
            name='content_right_panel',
            field=models.TextField(default=10000, max_length=10000),
            preserve_default=False,
        ),
    ]