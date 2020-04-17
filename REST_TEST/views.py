from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HellowWORLD(APIView):
    def get(self, request, format=None):
       
        an_apiview = [
            'dsdsdasdasdasdasd',
            'dasdasdasdasdasd23343',
            'dasda211d121fasfasdfafdasf',
        ]
        return Response({'messege': 'Hello!', 'an_apiview': an_apiview})