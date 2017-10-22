from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SonSerializer, UserSerializer, ScheduleSerializer, ActivitySerializer, PanicButtonCallSerializer
from .models import Parent, Son, Schedule, Activity, PanicButtonCall
from .permissions import IsOwner
from django.contrib.auth.models import User
#User views
class UserView(generics.ListCreateAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def perform_create(self, serializer):
            serializer.save()

class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


#Son views
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

#Schedule Views
class CreateScheduleView(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def perform_create(self, serializer):
            serializer.save()

class DetailsScheduleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

#Activity Views
class CreateActivityView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def perform_create(self, serializer):
            serializer.save()

class DetailsActivityView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

#PanicButtonCallViews
class CreatePanicButtonCallView(generics.ListCreateAPIView):
    queryset = PanicButtonCall.objects.all()
    serializer_class = PanicButtonCallSerializer

    def perform_create(self, serializer):
            serializer.save()

class DetailsPanicButtonCallView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PanicButtonCall.objects.all()
    serializer_class = PanicButtonCallSerializer

class Logout(APIView):
    queryset = User.objects.all()

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
