from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('playlists/', views.PlaylistList.as_view()),
    path('playlists/<int:pk>/', views.PlaylistDetail.as_view()),
    path('artists/', views.ArtistList.as_view()),
    path('artists/<int:pk>/', views.ArtistDetail.as_view()),
    path('musics/', views.MusicList.as_view()),
    path('musics/<int:pk>/', views.MusicDetail.as_view()),
    path('playlistcontents/', views.PlaylistContentList.as_view()),
    path('playlistcontents/<int:pk>/', views.PlaylistContentDetail.as_view()),
]