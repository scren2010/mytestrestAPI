from django.shortcuts import render
from rest_framework import request, status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import viewsets

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



class HelloWorldSETS(viewsets.ViewSet):
    def list(self, request):

        a = [
            "What is Lorem Ipsum? Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum ",
            "Why do we use it? It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).",
        ]
        return Response({"method":  'Dsktnb туда не знаю куда', 'a': a })
        