from rest_framework import serializers
from .models import Music, User, Playlist, Artist, PlaylistContent

class UserSerializer(serializers.ModelSerializer):
    followings_full = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'followings', 'followings_full', 'register_date', 'age']

    def get_followings_full(self, obj):
        return [{'id': e.id, 'name': e.name, 'genre': e.genre} for e in obj.followings.all() ]
    
    
class PlaylistSerializer(serializers.ModelSerializer):
    full_user = serializers.SerializerMethodField()
    
    class Meta:
        model = Playlist
        fields = ['id', 'name', 'description', 'user', 'full_user', 'create_date']

    def get_full_user(self, obj):
        return obj.user.username
        

class ArtistSerializer(serializers.ModelSerializer):
    follower = serializers.SerializerMethodField()
    music = serializers.SerializerMethodField()
    class Meta:
        model = Artist
        fields = ['id', 'name', 'password','genre', 'description', 'create_date', 'follower', 'music']

    def get_follower(self, obj):
        return [{'id': e.id, 'username': e.username} for e in obj.user_set.all()]
    
    def get_music(self, obj):
        return [{'id': e.id, 'title': e.title, 'album': e.album, 'genre': e.genre} for e in obj.music_set.all()]


class MusicSerializer(serializers.ModelSerializer):
    artist_full = serializers.SerializerMethodField()
    class Meta:
        model = Music
        fields = ['id', 'title', 'album', 'artist', 'genre', 'artist_full', 'release_date']
        # 未包含 release_date 字段

    def get_artist_full(self, obj):
        return [{'id': e.id, 'name': e.name} for e in obj.artist.all()]

class PlaylistContentSerializer(serializers.ModelSerializer):
    music_info = serializers.SerializerMethodField()
    class Meta:
        model = PlaylistContent
        fields = ['id', 'playlist', 'music', 'add_date', 'music_info']

    def get_music_info(self, obj):
        artist_name = [e.name for e in obj.music.artist.all()]
        return {'id': obj.music.id, 'title': obj.music.title, 'album': obj.music.album, 'artist': artist_name, 'genre': obj.music.genre}