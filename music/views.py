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