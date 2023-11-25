# Generated by Django 4.2.5 on 2023-11-12 04:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('channel', '0004_rename_url_channel_slug_alter_channel_theme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_parent', models.BooleanField(default=True)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('answers', models.ManyToManyField(blank=True, to='watch.comment')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_channel', to='channel.channel')),
                ('dislikes', models.ManyToManyField(blank=True, related_name='comment_dislikes', to='channel.channel')),
                ('likes', models.ManyToManyField(blank=True, related_name='comment_likes', to='channel.channel')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_video', to='channel.video')),
            ],
        ),
    ]
