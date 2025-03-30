from rest_framework import serializers
from .models import Music, User, Playlist, Artist, PlaylistContent

class UserSerializer(serializers.ModelSerializer):
    followings_full = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'followings', 'followings_full', 'age', 'role']
        extra_kwargs = {'password': {'write_only': True}}  # 确保密码仅用于写入

    def create(self, validated_data):
        # 处理多对多字段 followings
        followings_data = validated_data.pop('followings', None)
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()

        # 设置多对多关系
        if followings_data:
            instance.followings.set(followings_data)

        return instance

    def update(self, instance, validated_data):
        # 更新用户时也确保密码被哈希处理
        followings_data = validated_data.pop('followings', None)
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()

        # 更新多对多关系
        if followings_data:
            instance.followings.set(followings_data)
 
        return instance

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