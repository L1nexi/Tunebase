from .models import User, Playlist, Artist, Music, PlaylistEntry  # 修改引用
from .serializers import UserSerializer, PlaylistSerializer, ArtistSerializer, MusicSerializer, PlaylistEntrySerializer  # 修改引用
from rest_framework.viewsets import ModelViewSet
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.
class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['user__username', 'description']
    filterset_fields = ['user__username']

class MusicViewSet(ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    search_fields = ['title', 'album', 'artist__user__username', 'genre']
    filterset_fields = ['title', 'album', 'artist__user__username', 'genre']

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

class PlaylistEntryViewSet(ModelViewSet):  # 修改类名
    queryset = PlaylistEntry.objects.all()  # 修改模型引用
    serializer_class = PlaylistEntrySerializer  # 修改序列化器引用
    search_fields = ['playlist__name', 'music__title', 'music__artist__user__username', 'music__genre', 'music__album']
    filterset_fields = ['playlist']
