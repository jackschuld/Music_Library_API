# Generated by Django 4.1.6 on 2023-02-02 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_song_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
