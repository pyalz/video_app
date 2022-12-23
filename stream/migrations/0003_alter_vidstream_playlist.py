# Generated by Django 4.1.4 on 2022-12-23 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0002_vidstream_author_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vidstream',
            name='playlist',
            field=models.TextField(choices=[('playlist1', 'PLAYLIST1'), ('playlist2', 'PLAYLIST2'), ('playlist3', 'PLAYLIST3'), ('playlist4', 'PLAYLIST4'), ('playlist5', 'PLAYLIST5')], default='playlist1', max_length=30),
        ),
    ]
