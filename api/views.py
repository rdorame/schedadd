from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import ParentSerializer, SonSerializer, UserSerializer
from .models import Parent, Son
from .permissions import IsOwner
from django.contrib.auth.models import User

class CreateView(generics.ListCreateAPIView):
    """With this we can create new parents on our api"""
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new parent."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class CreateSonView(generics.ListCreateAPIView):
    """With this we can create new parents on our api"""
    queryset = Son.objects.all()
    serializer_class = SonSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
            """Save the post data when creating a new parent."""
            serializer.save(parentID=self.request.user)

class DetailsSonView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Son.objects.all()
    serializer_class = SonSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
