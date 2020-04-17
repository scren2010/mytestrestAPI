from django.shortcuts import render
from rest_framework import filters, request, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import authentication_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated



from .models import *
from .permissions import UpdateOwnProfile, PostOwnStatus
from .serializers import *


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


    serializer_class = HelloSerializer
    
    def list(self, request):

        a = [
            "What is Lorem Ipsum? Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum ",
            "Why do we use it? It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).",
        ]
        return Response({"method":  'Dsktnb туда не знаю куда', 'a': a })
    def create(self, request):
        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({"message": message})
        else: return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):

        return Response({"http_method": "GET"})
    
    def update(self, request, pk=None):

        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        
        return Response({"http_method": "PATCH"})


    def destroy(self, request, pk=None):
        return Response({"http_method": "delete"})


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class LoginViewSet(viewsets.ViewSet):
    
    serializer_class = AuthTokenSerializer

    def create(self, request):

        return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    permission_classes = (PostOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):

        serializer.save(user_profile=self.request.user)
    