# Generated by Django 4.1.6 on 2023-02-01 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Song',
            new_name='Songs',
        ),
    ]