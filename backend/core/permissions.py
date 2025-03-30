from rest_framework import permissions
from models import User, Playlist, Artist, Music, PlaylistContent

from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class IsAdminOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # 只允许管理员或对象的所有者修改

        if request.method in SAFE_METHODS:
            return True
        
        # 允许管理员访问
        if request.user.is_staff:
            return True
        
        # 允许对象的所有者访问
        if isinstance(obj, User):
            return obj == request.user
        elif isinstance(obj, Artist):
            return obj.user == request.user
        elif isinstance(obj, Music):
            return request.user in [artist.user for artist in obj.artist.all()]
        elif isinstance(obj, Playlist):
            return obj.user == request.user
        elif isinstance(obj, PlaylistContent):
            return obj.playlist.user == request.user
        return False