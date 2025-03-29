# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    # 自动主键作为 ID
    username = models.CharField(max_length=128, help_text="Enter a username")
    password = models.CharField(max_length=64, help_text="Enter a password")
    email = models.EmailField(max_length=128, help_text="Enter an email address")
    age = models.IntegerField(help_text="Enter an age", default=0)
    register_date = models.DateTimeField(auto_now_add=True)
    # 多对多关联：
    # 一个音乐家可能有多个粉丝，一个粉丝可能关注多个音乐家
    followings = models.ManyToManyField('Artist', blank=True)

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
    # 自动主键作为 ID
    name = models.CharField(max_length=64, help_text="Enter a musician name")
    password = models.CharField(max_length=64, help_text="Enter a password",default="")
    genre = models.CharField(max_length=64, help_text="Enter a genre",default="")
    description = models.TextField(help_text="Enter a description", null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    # follower = models.ManyToManyField(User)

    def __str__(self):
        return self.name
    
class Music(models.Model):
    # 自动主键作为 ID
    title = models.CharField(max_length=64, help_text="Enter a music name")
    album = models.CharField(max_length=64, help_text="Enter a album name",  null=True, blank=True)
    # 多对多关联：
    # 一个音乐可由多个音乐家创作，一个音乐家可创作多个音乐
    artist = models.ManyToManyField(Artist,blank=True)
    genre = models.CharField(max_length=64, help_text="Enter a genre", null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        res = f"{self.title} -"
        for e in self.artist.all():
            res += " " + e.name
        return res
    

class PlaylistContent(models.Model):
    # 自动主键作为 ID
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.playlist} - {self.music}"
    
    class Meta:
        unique_together = (('playlist', 'music'),)
    