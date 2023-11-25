# Generated by Django 4.2.5 on 2023-11-07 23:01

import apps.channel.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('avatar', models.URLField()),
                ('videos_qty', models.IntegerField(default=0)),
                ('playlists_qty', models.IntegerField(default=0)),
                ('banner', models.CharField(blank=True, max_length=255, null=True)),
                ('theme', models.CharField(choices=[('CLARO', 'Claro'), ('OSCURO', 'Oscuro'), ('DEVICE', 'Tema del dispositivo')], default='CLARO', max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_paused_history', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('thumbnail', models.ImageField(default='image_1.jpg', upload_to=apps.channel.models.thumbnail_directory_path)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('is_monetized', models.BooleanField(default=False)),
                ('is_for_everyone', models.BooleanField(default=True)),
                ('video', models.FileField(default='image_1.jpg', upload_to=apps.channel.models.video_directory_path)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_channel', to='channel.channel')),
                ('comments', models.ManyToManyField(blank=True, related_name='video_comments', to='channel.channel')),
                ('dislikes', models.ManyToManyField(blank=True, related_name='videl_dislikes', to='channel.channel')),
                ('likes', models.ManyToManyField(blank=True, related_name='video_likes', to='channel.channel')),
            ],
        ),
    ]
