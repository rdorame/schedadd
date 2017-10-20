from rest_framework import serializers
from .models import Son, Schedule, Activity, PanicButtonCall
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    sons = serializers.PrimaryKeyRelatedField(many=True, queryset=Son.objects.all())
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'sons')

class SonSerializer(serializers.ModelSerializer):

    parentID = serializers.ReadOnlyField(source='parentID.id')

    class Meta:
        model = Son
        fields = ('id', 'name', 'lastName', 'code', 'cellphone', 'parentID')
        read_only_fields = ('date_created', 'date_modified')

class ScheduleSerializer(serializers.ModelSerializer):
    activities = serializers.PrimaryKeyRelatedField(many=True, queryset=Schedule.objects.all())
    class Meta:
        model = Schedule
        fields = ('id', 'name', 'sonID', 'activities')
        read_only_fields = ('date_created', 'date_modified')

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'name', 'description', 'steps', 'imagePath', 'date', 'duration', 'scheduleID')
        read_only_fields = ('date_created', 'date_modified')

class PanicButtonCallSerializer(serializers.ModelSerializer):

    class Meta:
        model = PanicButtonCall
        fields = ('id', 'activityID', 'sonID', 'date_created')
        read_only_fields = ('date_created', 'date_modified')
