from rest_framework import serializers
from .models import Song

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'release_date', 'genre']