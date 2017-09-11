from rest_framework import serializers
from .models import Parent, Son
from django.contrib.auth.models import User

class ParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parent
        fields = ('id', 'name', 'lastName', 'mail', 'password', 'cellphone')
        read_only_fields = ('date_created', 'date_modified')

class SonSerializer(serializers.ModelSerializer):

    parentID = serializers.ReadOnlyField(source='parentID.id')

    class Meta:
        model = Son
        fields = ('id', 'name', 'lastName', 'code', 'cellphone', 'parentID')
        read_only_fields = ('date_created', 'date_modified')

class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    sons = serializers.PrimaryKeyRelatedField(many=True, queryset=Son.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'sons', 'email', 'password')
