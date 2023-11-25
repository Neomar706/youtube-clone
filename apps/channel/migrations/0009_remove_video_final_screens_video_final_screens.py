# Generated by Django 4.2.5 on 2023-11-25 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0008_video_final_screens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='final_screens',
        ),
        migrations.AddField(
            model_name='video',
            name='final_screens',
            field=models.ManyToManyField(null=True, to='channel.video'),
        ),
    ]