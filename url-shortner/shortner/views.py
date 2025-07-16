from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ShortURL
from .serializers import ShortURLSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect # fro redirection

@api_view(['POST'])
def create_short_url(request):
    serializer = ShortURLSerializer(data=request.data)
    if serializer.is_valid():
        short_url = serializer.save()
        return Response(ShortURLSerializer(short_url).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def retrieve_original_url(request, short_code):
    short_url = get_object_or_404(ShortURL, shortCode=short_code)
    short_url.accessCount += 1
    short_url.save()
    # return Response(ShortURLSerializer(short_url).data) This will return JSON object by whiich we can manually redierect by extrecting thr url
    return HttpResponseRedirect(short_url.url) #this will directly redirect to the original url
