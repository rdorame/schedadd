from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import SonSerializer, UserSerializer
from .models import Parent, Son
from .permissions import IsOwner
from django.contrib.auth.models import User

class CreateSonView(generics.ListCreateAPIView):
    queryset = Son.objects.all()
    serializer_class = SonSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
            serializer.save(parentID=self.request.user)

class DetailsSonView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Son.objects.all()
    serializer_class = SonSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def perform_create(self, serializer):
            serializer.save()


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
