from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistViewSet, MusicViewSet, UserViewSet, PlaylistViewSet, PlaylistContentViewSet

router = DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'musics', MusicViewSet)
router.register(r'users', UserViewSet)
router.register(r'playlists', PlaylistViewSet)
router.register(r'playlist-contents', PlaylistContentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]