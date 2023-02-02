from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongsSerializer
from .models import Song


@api_view(['GET', 'POST'])
def music_list(request):
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongsSerializer(songs, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = SongsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'GET':
        serializer = SongsSerializer(song)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SongsSerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def song_like(request, pk):
    if request.method == 'PUT':
        song = get_object_or_404(Song, pk=pk)
        song.likes += 1
        song_serializer = SongsSerializer(song)
        serializer = SongsSerializer(song, song_serializer.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response(status=status.HTTP_202_ACCEPTED)
    
