from django.contrib import admin
from .models import User, Playlist, Artist, Music, PlaylistContent

# Register your models here.
admin.site.register(User)
admin.site.register(Playlist)
admin.site.register(Artist)
admin.site.register(Music)
admin.site.register(PlaylistContent)
