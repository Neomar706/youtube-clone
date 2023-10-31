# Generated by Django 4.2.5 on 2023-10-31 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0007_playlist'),
        ('playlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channel.channel'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='videos',
            field=models.ManyToManyField(blank=True, to='channel.video'),
        ),
    ]
