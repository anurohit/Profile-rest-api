#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets

# Create your views here.

class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView"""

        an_apiview = [
            'Uses HTTP method as function (get,post,patch,put,delete)',
            'Is similar to a traditional django view',
            'Gives most control over ypur applicationlogic',
            'Is mapped manually to URLS',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        """Create a Hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self,request,pk=None):
        """Handles updating an object"""
        return Response({'method': 'PUT'})

    def patch(self,request,pk=None):
        """Handles partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self,request,pk=None):
        """Handles deleting object"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer
    def list(self,request):

        a_viewset = [
            'Uses actions(list,create,reterieve,update,partial_update)',
            'Automatically maps to URL using routers',
            'Provides more functionality with less code',
        ]
        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self,request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'

            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):

        return Response({'http_method': 'GET'})

    def update(self,request,pk=None):

        return Response({'http_method': 'PUT'})

    def partial_update(self,request,pk=None):

        return Response({'http_method': 'PATCH'})

    def destroy(self,request,pk=None):

        return Response({'http_method': 'DELETE'})
