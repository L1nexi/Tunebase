from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Playlist, Artist, Music, PlaylistEntry

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'role', 'followings')}),
    )
    list_display = UserAdmin.list_display + ('role',)

admin.site.register(Artist)
admin.site.register(Playlist)
admin.site.register(Music)
admin.site.register(PlaylistEntry)
