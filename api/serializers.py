from rest_framework import serializers
from .models import Son
from django.contrib.auth.models import User

class SonSerializer(serializers.ModelSerializer):

    parentID = serializers.ReadOnlyField(source='parentID.id')

    class Meta:
        model = Son
        fields = ('id', 'name', 'lastName', 'code', 'cellphone', 'parentID')
        read_only_fields = ('date_created', 'date_modified')

class UserSerializer(serializers.ModelSerializer):
    sons = serializers.PrimaryKeyRelatedField(many=True, queryset=Son.objects.all())
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'sons')
