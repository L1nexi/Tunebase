from rest_framework import serializers
from .models import Music, User, Playlist, Artist, PlaylistContent

class UserSerializer(serializers.ModelSerializer):
    followings_full = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'followings', 'followings_full', 'age', 'role']

    def get_followings_full(self, obj):
        return [{'id': e.id, 'name': e.user.username, 'genre': e.genre} for e in obj.followings.all()]
    

class PlaylistSerializer(serializers.ModelSerializer):
    full_user = serializers.SerializerMethodField()
    
    class Meta:
        model = Playlist
        fields = ['id', 'name', 'description', 'user', 'full_user', 'create_date']

    def get_full_user(self, obj):
        return {'id': obj.user.id, 'username': obj.user.username}
        

class ArtistSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # 嵌套 UserSerializer
    follower = serializers.SerializerMethodField()
    music = serializers.SerializerMethodField()
    class Meta:
        model = Artist
        fields = ['id', 'user', 'genre', 'description', 'follower', 'music']

    def get_follower(self, obj):
        return [{'id': e.id, 'username': e.username} for e in obj.followers.all()]
    
    def get_music(self, obj):
        return [{'id': e.id, 'title': e.title, 'album': e.album, 'genre': e.genre} for e in obj.music_set.all()]


class MusicSerializer(serializers.ModelSerializer):
    artist_full = serializers.SerializerMethodField()
    class Meta:
        model = Music
        fields = ['id', 'title', 'album', 'artist', 'genre', 'artist_full', 'release_date']

    def get_artist_full(self, obj):
        return [{'id': e.id, 'name': e.user.username} for e in obj.artist.all()]


class PlaylistContentSerializer(serializers.ModelSerializer):
    music_info = serializers.SerializerMethodField()
    class Meta:
        model = PlaylistContent
        fields = ['id', 'playlist', 'music', 'add_date', 'music_info']

    def get_music_info(self, obj):
        artist_name = [e.user.username for e in obj.music.artist.all()]
        return {'id': obj.music.id, 'title': obj.music.title, 'album': obj.music.album, 'artist': artist_name, 'genre': obj.music.genre}