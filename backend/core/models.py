# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('artist', 'Artist'),
    ]
    age = models.IntegerField(help_text="Enter an age", default=0)
    followings = models.ManyToManyField('Artist', blank=True, related_name='followers')  # 添加 related_name
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user', help_text="Select a role")

    def __str__(self):
        return self.username

class Playlist(models.Model):
    # 自动主键作为 ID
    name = models.CharField(max_length=64, help_text="Enter a playlist name")
    description = models.TextField(help_text="Enter a description", null=True, blank=True)
    # 多对一关联：
    # 一个播放列表由一个用户创建，一个用户可创建多个播放列表
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.user}"
    
class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='artist_profile')
    genre = models.CharField(max_length=64, help_text="Enter a genre", default="")
    description = models.TextField(help_text="Enter a description", null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Music(models.Model):
    # 自动主键作为 ID
    title = models.CharField(max_length=64, help_text="Enter a music name")
    album = models.CharField(max_length=64, help_text="Enter a album name",  null=True, blank=True)
    # 多对多关联：
    # 一个音乐可由多个音乐家创作，一个音乐家可创作多个音乐
    artist = models.ManyToManyField(Artist, blank=True)
    genre = models.CharField(max_length=64, help_text="Enter a genre", null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        res = f"{self.title} -"
        for e in self.artist.all():
            res += " " + e.user.username
        return res
    

class PlaylistEntry(models.Model):  # 修改类名
    # 自动主键作为 ID
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.playlist} - {self.music}"
    
    class Meta:
        unique_together = (('playlist', 'music'),)
