from .models import User, Playlist, Artist, Music, PlaylistContent
from .serializers import UserSerializer, PlaylistSerializer, ArtistSerializer, MusicSerializer, PlaylistContentSerializer
from rest_framework import generics
from django_filters import rest_framework
from rest_framework import filters
# Create your views here.
class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    filter_backends = [filters.SearchFilter, rest_framework.DjangoFilterBackend]
    search_fields = ['name', 'description']
    filterset_fields = ['name']

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class MusicList(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

    filter_backends = [filters.SearchFilter, rest_framework.DjangoFilterBackend]
    search_fields = ['title', 'album', 'artist__name','genre']
    filterset_fields = ['title', 'album', 'artist__name','genre']


class MusicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = [filters.SearchFilter, rest_framework.DjangoFilterBackend]
    search_fields = ['username']
    filterset_fields = ['username']
    


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PlaylistList(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    filter_backends = [filters.SearchFilter, rest_framework.DjangoFilterBackend]
    search_fields = ['name', 'description', 'user__username']
    filterset_fields = ['name', 'user']


class PlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class PlaylistContentList(generics.ListCreateAPIView):
    queryset = PlaylistContent.objects.all()
    serializer_class = PlaylistContentSerializer

    filter_backends = [filters.SearchFilter, rest_framework.DjangoFilterBackend]      # 启用对 playlist 的过滤
    filterset_fields = ['playlist']
    search_fields = ['playlist__name', 'music__title', 'music__artist__name', 'music__genre', 'music__album']


# 对播放列表，不存在修改操作，只需要进行列表的增加和删除
class PlaylistContentDetail(generics.RetrieveDestroyAPIView):
    queryset = PlaylistContent.objects.all()
    serializer_class = PlaylistContentSerializer
