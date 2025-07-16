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


@api_view(['PUT'])
def update_short_url(request, short_code):
    short_url = get_object_or_404(ShortURL, shortCode=short_code)
    serializer = ShortURLSerializer(short_url, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_short_url(request, short_code):
    short_url = get_object_or_404(ShortURL, shortCode=short_code)
    short_url.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def url_statistics(request, short_code):
    short_url = get_object_or_404(ShortURL, shortCode=short_code)
    return Response(ShortURLSerializer(short_url).data)


@api_view(['GET'])
def list_all_urls(request):
    urls = ShortURL.objects.all().order_by('-createdAt')
    serializer = ShortURLSerializer(urls, many=True)
    return Response(serializer.data)