# Generated by Django 3.0.5 on 2021-01-28 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quarterlyfilerview',
            old_name='filerDecription',
            new_name='filerDescription',
        ),
    ]
