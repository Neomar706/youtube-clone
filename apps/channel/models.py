from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from uuid import uuid4 as uuid
from apps.playlist.models import Playlist


User = get_user_model()

banner_choices = [
    ('CLARO', 'Claro'),
    ('OSCURO', 'Oscuro'),
    ('DEVICE', 'Tema del dispositivo')
]


def thumbnail_directory_path(instance, filename):
    extension = filename.split('.')[-1]
    return 'thumbnails/{0}/{1}.{2}'.format(instance.channel.user, uuid(), extension)

def video_directory_path(instance, filename):
    extension = filename.split('.')[-1]
    return 'videos/{0}/{1}.{2}'.format(instance.channel.user, uuid(), extension)


class Channel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='channel_user')
    videos_qty = models.IntegerField(default=0)
    playlists_qty = models.IntegerField(default=0)
    suscribers = models.ManyToManyField('self', blank=True)
    banner = models.CharField(max_length=255, blank=True, null=True)
    theme = models.CharField(max_length=100, choices=banner_choices, default='CLARO')
    welcome_video = models.OneToOneField('Video', blank=True, null=True, on_delete=models.CASCADE, related_name='welcome_video_channel')
    created_at = models.DateTimeField(default=timezone.now)
    is_paused_history = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    url = models.URLField()

    def __str__(self):
        return 'channel/{0} - {1}'.format(self.id, self.user.username)


class Video(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='video_channel')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to=thumbnail_directory_path, default='image_1.jpg')
    duration = models.DurationField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    is_monetized = models.BooleanField(default=False)
    is_for_everyone = models.BooleanField(default=True)
    views = models.ManyToManyField(Channel, blank=True, related_name='video_views')
    likes = models.ManyToManyField(Channel, blank=True, related_name='video_likes')
    dislikes = models.ManyToManyField(Channel, blank=True, related_name='videl_dislikes')
    comments = models.ManyToManyField(Channel, blank=True, related_name='video_comments')
    playlists = models.ManyToManyField(Playlist, blank=True, related_name='video_playlists')
    video = models.FileField(upload_to=video_directory_path, default='image_1.jpg')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'channel/{0} - {1} - {2}'.format(self.channel.id, self.channel.user.username, self.title)


class Playlist(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='playlist_channel')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to=thumbnail_directory_path, default='image_1.jpg')
    duration = models.DurationField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    videos = models.ManyToManyField(Video, blank=True, related_name='video_playlists')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'channel/{0} - {1} - {2}'.format(self.channel.id, self.channel.user.username, self.title)

    

@receiver(post_save, sender=User)
def save_channel(sender, instance, created, **kwargs):
    if created:
        Channel.objects.create(user=instance, 
                               is_active=True)



