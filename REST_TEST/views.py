from django.shortcuts import render
from rest_framework import request, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import HelloSerializer


class HellowWORLD(APIView):

    serializer_class = HelloSerializer

    def get(self, request, format=None):
       
        an_apiview = [
            'dsdsdasdasdasdasd',
            'dasdasdasdasdasd23343',
            'dasda211d121fasfasdfafdasf',
        ]
        return Response({'messege': 'Hello!', 'an_apiview': an_apiview})
    def post(self, request):
        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            messege = "Привет сукчка {0}".format(name)

            return Response({"message": messege})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk=None):

        return Response({'method': 'put'})

    def patch(self, request, pk=None):

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        return Response({'method': 'delete'})