from .models import User, Playlist, Artist, Music, PlaylistContent
from .serializers import UserSerializer, PlaylistSerializer, ArtistSerializer, MusicSerializer, PlaylistContentSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    search_fields = ['name', 'description']
    filterset_fields = ['name']

class MusicViewSet(ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    search_fields = ['title', 'album', 'artist__name', 'genre']
    filterset_fields = ['title', 'album', 'artist__name', 'genre']

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ['username']
    filterset_fields = ['username']

class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    search_fields = ['name', 'description', 'user__username']
    filterset_fields = ['name', 'user']

class PlaylistContentViewSet(ModelViewSet):
    queryset = PlaylistContent.objects.all()
    serializer_class = PlaylistContentSerializer
    search_fields = ['playlist__name', 'music__title', 'music__artist__name', 'music__genre', 'music__album']
    filterset_fields = ['playlist']
