# Generated by Django 4.2.5 on 2023-12-22 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='videos',
            new_name='video',
        ),
    ]