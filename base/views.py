from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerialize
from .models import User
from base import serializers


@api_view(['GET'])
def getRoutes(request):
    routes = [
         {
            'Endpoint':'/users/create/',
            'method':'POST',
            'body': {'body':""},
            'description': 'Return an array of notes'
        },
        {
            'Endpoint':'/users/id/update/',
            'method':'PUT',
            'body': {'body':""},
            'description': 'Create an existing note with data sent in'
        },
        {
            'Endpoint':'/users/ads/create',
            'method':'POST',
            'body': {'body':""},
            'description': 'Return an array of notes'
        },
        {
            'Endpoint':'/users/ads/id/update/',
            'method':'PUT',
            'body': {'body':""},
            'description': 'Create an existing note with data sent in'
        },
        {
            'Endpoint':'/users/ads/id/delete/',
            'method':'DELETE',
            'body': None,
            'description': 'Deletes an existing ad'
        },
        {
            'Endpoint':'/users/ads',
            'method':'GET',
            'body': None,
            'description': 'Return a ads object'
        },
     ]
    return Response(routes)


@api_view(['GET'])
def getads(request):
    users = User.ads.objects.all()
    serializer = NoteSerialize(users, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
    data = request.data

    user = User.objects.create(
        body = data['body']
    )
    serializer = NoteSerialize(user, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createads(request):
    data = request.data

    user = User.ads.objects.create(
        body = data['body']
    )
    serializer = NoteSerialize(user, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateUser(request,pk):
    data = request.data

    user = User.objects.get(id=pk)
    serializer = NoteSerialize(user, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def updateads(request,pk):
    data = request.data

    user = User.ads.objects.get(id=pk)
    serializer = NoteSerialize(user, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteads(request,pk):
    user= User.ads.objects.get(id=pk)
    user.delete()
    return Response('Note was Deleted !')