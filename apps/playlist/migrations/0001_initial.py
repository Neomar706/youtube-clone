# Generated by Django 4.2.4 on 2023-10-26 02:21

import apps.playlist.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('channel', '0005_remove_playlist_channel_remove_playlist_videos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('thumbnail', models.ImageField(default='image_1.jpg', upload_to=apps.playlist.models.thumbnail_directory_path)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlist_channel', to='channel.channel')),
                ('videos', models.ManyToManyField(blank=True, related_name='video_playlists', to='channel.video')),
            ],
        ),
    ]
